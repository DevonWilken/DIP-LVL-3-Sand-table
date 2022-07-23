from unittest import skip
import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivymd.utils.fitimage import FitImage
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard
from functools import partial
from kivy.properties import ObjectProperty
import time
import serial
from threading import Thread
Window.size = (1024, 600)
Navigation_kv = '''
<Navigation>:
    BoxLayout:
        orientation:'vertical'
        ##Navigation bar at bottom
        MDBottomNavigation:
            panel_color: .2, .2, .2, 1

            ##bottom left play circle icon
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Playing'
                icon: "play-circle"
                ##playing screen
                Playing:                   

            ##Middle playlist icon in navigation bar
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Plalists'
                icon: 'playlist-plus'
                ##Playlist screen
                Playlist:

            ##lighting icon in bottom nav bar
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Lighting'
                icon: 'flare'
                ##lighting screen
                Lighting:
        '''
image_list = []
playlist_15_min = [["Gcode\Spiral\Spiral.png","Gcode\Spiral\Spiral Inwards.gcode", "Gcode\Spiral\Spiral Outwards.gcode"], ["Gcode\SpiralWeb\Spiral Web.png", "Gcode\SpiralWeb\Spiral Web Inwards.gcode", "Gcode\SpiralWeb\Spiral Web Outwards.gcode"], ["Gcode\Square\Square.png", "Gcode\Square\Square Inward.gcode", "Gcode\Square\Square Outward.gcode"]]
list_of_lists = []
state = ["play 1"]
light_state = [""]
def play_gcode(file, list_of_lists, state):
    s = serial.Serial('COM4',115200)
    s.set_buffer_size(rx_size = 1, tx_size = 1)
    
    # Open g-code file
    f = open(file,'r')
    for line in f:
            l = line.strip() # Strip all EOL characters for consistency
            if l == "$H" or l == "" or l.find(";") != -1:
                pass
            else:
                striped_l = l.strip("G0 ") #remove speed function G0
                number_strings = striped_l.split() # Split the line on runs of whitespace
                list_of_lists.append(number_strings) #add to list

    for item in list_of_lists:
        for i in item:
            removed_x_y = i[1:]#remove first character X or Y
            if float(removed_x_y) > 370:#check boundry
                print("Gcode file exceeds boundry of 370mm please use files under 370mm")
                print("code will now exit")
                time.sleep(5)
                raise SystemExit
            else:
                f = open(file,'r')
                # Open grbl serial port
                # Wake up grbl
                s.write("\r\n\r\n".encode())
                time.sleep(2)   # Wait for grbl to initialize 
                s.flushInput()  # Flush startup text in serial input


                # Stream g-code to grbl
                s.write(("$H" + '\n').encode())
                grbl_out = s.readline() # Wait for grbl response with carriage return
                print( 'homing: ' + (grbl_out.strip()).decode())
                for line in f:
                    l = line.strip() # Strip all EOL characters for consistency
                    if l.startswith(";") == True:
                        skip
                    else:
                        print( 'Sending: ' + l)
                        s.write((l + '\n').encode()) # Send g-code block to grbl
                        grbl_out = s.readline() # Wait for grbl response with carriage return
                        print( ' : ' + (grbl_out.strip()).decode())
                        print(state)  
                        while True:
                            if state[0] == "pause":
                                s.write(("!" + '\n').encode()) # Send g-code block to grbl
                                if state[0] == "play":
                                    s.write(("~" + '\n').encode()) # Send g-code block to grbl
                                    break
                            elif state[0] == "pause 2":
                                s.write(("!" + '\n').encode()) # Send g-code block to grbl
                                s.close
                                f.close
                                return None
                            elif state[0] == "play 1":
                                print("break")
                                break
                           
                            



                # Wait here until grbl is finished to close serial port and file.
                input("  Press <Enter> to exit and disable grbl.") 

                # Close file and serial port
                f.close()
                s.close
    
playing_image_source = ""

class Navigation(BoxLayout):
    pass
class Playing(Widget):
    playlist_15_min = [["Gcode\Spiral\Spiral.png","Gcode\Spiral\Spiral Inwards.gcode", "Gcode\Spiral\Spiral Outwards.gcode"], ["Gcode\SpiralWeb\Spiral Web.png", "Gcode\SpiralWeb\Spiral Web Inwards.gcode", "Gcode\SpiralWeb\Spiral Web Outwards.gcode"], ["Gcode\Square\Square.png", "Gcode\Square\Square Inward.gcode", "Gcode\Square\Square Outward.gcode"]]
    def __init__(self, **kwargs):
        self.playlist_no = 0
        playing_image_source = self.playlist_15_min[self.playlist_no][0]
        self.float_layout = FloatLayout()
        #self.bar = ProgressBar(min= 0, max= 1, size_hint= (None, None), size= (350, 5), pos= (565, 270))
        self.fav = MDIconButton(icon= "heart-outline", user_font_size= "40sp", pos= (705, 300), on_press = self.favorite)
        self.rept = MDIconButton(icon= "repeat", user_font_size= "40sp", pos= (555, 300), on_press= self.repeat)
        self.lab = Label(text="Shuffle on",font_size= "10sp",pos= (840, 260))
        self.shuf = MDIconButton(icon= "shuffle", user_font_size= "40sp", pos= (855, 300), on_press = self.shuffle)
        self.play = MDIconButton(icon= 'play-circle', user_font_size= "50sp", pos= (700, 175), on_press = self.play_button)
        self.prev = MDIconButton(icon= 'rewind', user_font_size= "50sp", pos= (550, 175), on_press = self.previous)  
        self.next = MDIconButton(icon= 'fast-forward', user_font_size= "50sp", pos= (850, 175), on_press = self.skip)
        self.playing_image = FitImage(source= playing_image_source , size_hint = (None, None), size = (400, 400), pos= (80, 70))
        image_list.append(self.playing_image)
        super(Playing, self).__init__(**kwargs)
        self.add_widget(self.float_layout)
        self.float_layout.add_widget(self.fav)
        self.float_layout.add_widget(self.rept)
        self.float_layout.add_widget(self.lab)
        self.float_layout.add_widget(self.shuf)
        self.float_layout.add_widget(self.play)
        self.float_layout.add_widget(self.prev)
        self.float_layout.add_widget(self.next)
        self.float_layout.add_widget(self.playing_image)
    def play_button(self, event):
        if self.play.icon == "play-circle":
            self.play.icon = "pause-circle"
            if state[0] == "play":
                pass
            elif state[0] == "play 1":
                playing_t = Thread(target= play_gcode, args= (self.playlist_15_min[self.playlist_no][1], list_of_lists, state))
                playing_t.start()
            elif state[0] == "pause":
                state[0] = "play"
            elif state[0] == "pause 2":
                playing_t = Thread(target= play_gcode, args= (self.playlist_15_min[self.playlist_no][1], list_of_lists, state))
                playing_t.start()
                state[0] = "play 1"
        elif self.play.icon == "pause-circle":
            self.play.icon = "play-circle"
            state[0] = "pause"

    def skip(self, event):
        state[0] = "pause 2"
        self.play.icon = "play-circle"
        self.playlist_no = self.playlist_no + 1
        if self.playlist_no >= 2:
            self.playlist_no = -1
        self.playing_image.source =  self.playlist_15_min[self.playlist_no][0]
    def previous(self, event):
        state[0] = "pause 2"
        self.play.icon = "play-circle"
        self.playlist_no = self.playlist_no - 1
        if self.playlist_no <= 0:
            self.playlist_no = 2
        self.playing_image.source =  self.playlist_15_min[self.playlist_no][0]


    def favorite(self, event):
        if self.fav.icon == "heart-outline":
            self.fav.icon = "heart"
        elif self.fav.icon == "heart":
            self.fav.icon = "heart-outline"
    def shuffle(self, event):
        if self.lab.text == "Shuffle on":
            self.lab.text = "Shuffle off"
        elif self.lab.text == "Shuffle off":
            self.lab.text = "Shuffle on"
    def repeat(self, event):
        if self.rept.icon == "repeat":
            self.rept.icon = "repeat-off"
        elif self.rept.icon == "repeat-off":
            self.rept.icon = "repeat"

class Playlist(BoxLayout):
    def __init__(self, **kwargs): 
        super(Playlist, self).__init__(**kwargs)   
        #title 15 min and scroll
        self.box_1 = BoxLayout(orientation='horizontal')
        self.scroll_1 = ScrollView(size=self.size)
        self.grid_1 =GridLayout(size_hint_y=None, height=self.minimum_height, width=self.minimum_width, cols=1, spacing="20dp", padding= "10dp")
        self.card_15_min = MDCard(orientation="vertical", size_hint= (None, None), size= ("450dp", "20dp"), md_bg_color= (.2, .2, .2, 1), radius= [15])
        self.card_15_min_lab = MDLabel(text= "15 Min patterns", text_color= (1, 1, 1, 1), halign= "center")
        self.grid_2 = GridLayout(size_hint_y=None, height=self.minimum_height, width=self.minimum_width, cols=2, spacing="20dp", padding="20dp")

        #title 45min and scroll
        self.scroll_2 = ScrollView(size=self.size)
        self.grid_3 =GridLayout(size_hint_y=None, height=self.minimum_height, width=self.minimum_width, cols=1, spacing="20dp", padding= "10dp")
        self.card_45_min = MDCard(orientation="vertical", size_hint= (None, None), size= ("450dp", "20dp"), md_bg_color= (.2, .2, .2, 1), radius= [15])
        self.card_45_min_lab = MDLabel(text= "45 Min patterns", text_color= (1, 1, 1, 1), halign= "center")
        self.grid_4 = GridLayout(size_hint_y=None, height=self.minimum_height, width=self.minimum_width, cols=2, spacing="20dp", padding="20dp")
  
        self.add_widget(self.box_1)
        #title 15 min and scroll
        self.box_1.add_widget(self.scroll_1)
        self.scroll_1.add_widget(self.grid_1)
        self.grid_1.add_widget(self.card_15_min)
        self.card_15_min.add_widget(self.card_15_min_lab)
        self.grid_1.add_widget(self.grid_2)
        #pattern cards
        for item in playlist_15_min:
            number = playlist_15_min.index(item)
            self.card_1 = MDCard(orientation="vertical", size_hint= (None, None), size= ("200dp", "200dp"), radius=[15])
            self.box_2 = BoxLayout(orientation="horizontal", pos_hint= { "center_x": 0.5, "center_y": 0.5 })
            self.title_lab = MDLabel(text= "Spiral", pos_hint= { "center_x": 0.5, "center_y": 0.5 }, text_color= (1, 1, 1, 1))
            self.switch_but =MDIconButton(icon= 'toggle-switch', pos_hint= { "center_x": 0.5, "center_y": 0.5 }, user_font_size= "20sp",on_press= self.starting_position)
            self.card_2 = MDCard(pos_hint= { "center_x": 0.5, "center_y": 0.5 }, orientation="vertical", size_hint= (None, None), size= ("150dp", "150dp"), 
                radius=[15], ripple_behavior= True)
            
            self.card_image = FitImage(pos_hint= { "center_x": 0.5, "center_y": 0.5 }, source= item[0], size_hint= (None, None), size= (140, 140))
            self.box_3 =BoxLayout(orientation="horizontal", padding= "60dp")
            self.pos_label =MDLabel(text= "Outwards", text_color= (1, 1, 1, 1), pos_hint= { "center_x": 0.5, "center_y": 0.5 })

            self.card_1.add_widget(self.box_2)
            self.box_2.add_widget(self.title_lab)
            self.box_2.add_widget(self.switch_but)
            self.card_1.add_widget(self.card_2)
            self.card_2.add_widget(self.card_image)
            self.card_1.add_widget(self.box_3)
            self.box_3.add_widget(self.pos_label)
            self.grid_2.add_widget(self.card_1)
                #add card to grid
            self.card_2.bind(on_press = self.play_selected_image)



        #title 45min and scroll
        self.box_1.add_widget(self.scroll_2)
        self.scroll_2.add_widget(self.grid_3)
        self.grid_3.add_widget(self.card_45_min)
        self.card_45_min.add_widget(self.card_45_min_lab)
        self.grid_3.add_widget(self.grid_4)
        
        


    def starting_position(self, instance): 
        if instance.parent.parent.children[0].children[0].text == "Outwards":
            instance.parent.parent.children[0].children[0].text = "Inwards"
            instance.icon = "toggle-switch-off"
        elif instance.parent.parent.children[0].children[0].text == "Inwards":

            instance.parent.parent.children[0].children[0].text = "Outwards"
            instance.icon = "toggle-switch"
    

    def play_selected_image(self, instance):
        image_list[0].source = instance.children[-1].children[0].source

class Lighting(BoxLayout):
    def __init__(self, **kwargs): 
        super(Lighting, self).__init__(**kwargs) 
        self.light_btn= Button(text = "LED OFF", size_hint = (1, 1), background_color =(0, 0, 0, 0))
        self.light_btn.bind(on_press = self.light)
        self.add_widget(self.light_btn)

    def light(self, instance):
        if instance.text == "LED OFF":
            instance.background_color = (1, 1, 1, 1)
            instance.text = "LED ON"

            if state[0] == "pause":
                state[0] = "play_1"
        elif instance.text == "LED ON":
            instance.background_color = (0, 0, 0, 0)
            instance.text = "LED OFF"

            if state[0] == "pause":
                state[0] = "play_1"


class Test(MDApp): 
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        Builder.load_string(Navigation_kv)
        return Navigation()



if __name__ == '__main__':
    Test().run()
