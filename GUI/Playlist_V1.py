from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button

Window.size = (1024, 600)

class Navigation(BoxLayout):
    def shuffle(self):
        if self.ids.shuffle.text == "Shuffle on":
            self.ids.shuffle.text = "Shuffle off"
        else:
            self.ids.shuffle.text = "Shuffle on"
    def starting_position(self):
        if self.ids.label.text == "Outwards":
            self.ids.label.text = "Inwards"
            self.ids.switch.icon = "toggle-switch-off"
        else:
            self.ids.label.text = "Outwards"
            self.ids.switch.icon = "toggle-switch"

class Test(MDApp): 
    def play(self):
        print("play") 
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        Builder.load_string(
'''
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

                BoxLayout:
                    orientation: "vertical"

                    MDFloatLayout:    
                        ProgressBar:
                            id: my_progress_bar
                            min: 0
                            max: 1
                            size_hint: None, None
                            size: 350, 5
                            pos: 565, 270

                    MDFloatLayout:
                        FitImage:
                            source: "Gcode\Spiral Web\Spiral Web.png"
                            size_hint: None, None
                            size: 400, 400
                            pos: 80, 70
                            
                    MDFloatLayout:
                        MDIconButton:
                            icon: "rewind"
                            user_font_size: "50sp"
                            pos: 550, 175
                    
                    MDFloatLayout:
                        MDIconButton:
                            id: "play"
                            icon: 'play-circle'
                            user_font_size: "50sp"
                            pos: 700, 175
                            on_press: 
                                if self.icon == "play-circle": app.play(); self.icon = "pause-circle"
                                else: self.icon = "play-circle"
                            

                            
                    MDFloatLayout:
                        MDIconButton:
                            icon: 'fast-forward'
                            user_font_size: "50sp"
                            pos: 850, 175
                    
                    
                    MDFloatLayout:
                        MDIconButton:
                            icon: "heart-outline"
                            user_font_size: "40sp"
                            pos: 705, 300
                            on_press:
                                if self.icon == "heart-outline" : self.icon = "heart"
                                else: self.icon = "heart-outline"
                    
                    MDFloatLayout:
                        MDIconButton:
                            icon: "repeat"
                            user_font_size: "40sp"
                            pos: 555, 300
                            on_press:
                                if self.icon == "repeat" : self.icon = "repeat-off"
                                else: self.icon = "repeat"
                    
                    MDFloatLayout:
                        MDLabel:
                            id: shuffle
                            text: "Shuffle on"
                            font_size: "10sp"
                            pos: 865, 280
                        MDIconButton:
                            id: shuffle_icon
                            icon: "shuffle"
                            user_font_size: "40sp"
                            pos: 855, 300
                            on_press: root.shuffle()         




            ##Middle playlist icon in navigation bar
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Plalists'
                icon: 'playlist-plus'
                ##Playlist screen

                BoxLayout:
                    orientation:'horizontal' 
                    ##Playlist on left for 15 min patterns
                    ScrollView:
                        size:self.size
                        GridLayout:
                            size_hint_y:None
                            height:self.minimum_height
                            width:self.minimum_width
                            cols:1
                            spacing:"20dp"
                            padding: "10dp"
                            
                            MDCard:
                                orientation:"vertical"
                                size_hint: None, None
                                size: "450dp", "20dp"
                                md_bg_color: .2, .2, .2, 1
                                radius:[15]
                                MDLabel:
                                    text: "15 Min patterns"
                                    text_color: 1, 1, 1, 1
                                    halign: "center"

                            GridLayout:
                                size_hint_y:None
                                height:self.minimum_height
                                width:self.minimum_width
                                cols:2
                                spacing:"20dp"
                                padding:"20dp"


                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }

                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                
                                


                                    



                    ##45 min playlist section on right
                    ScrollView:
                        size:self.size
                        GridLayout:
                            size_hint_y:None
                            height:self.minimum_height
                            width:self.minimum_width
                            cols:1
                            spacing:"20dp"
                            padding:"20dp"
                            
                            MDCard:
                                orientation:"vertical"
                                size_hint: None, None
                                size: "450dp", "20dp"
                                md_bg_color: .2, .2, .2, 1
                                radius:[15]
                                MDLabel:
                                    text: "45 Min patterns"
                                    text_color: 1, 1, 1, 1
                                    halign: "center"

                            GridLayout:
                                size_hint_y:None
                                height:self.minimum_height
                                width:self.minimum_width
                                cols:2
                                spacing:"20dp"
                                padding:"20dp"

                        
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                MDCard:
                                    orientation:"vertical"
                                    size_hint: None, None
                                    size: "200dp", "200dp"
                                    radius:[15]
                                    
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        MDLabel:
                                            text: "Spiral"
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            text_color: 1, 1, 1, 1
                                        MDIconButton:
                                            id: switch
                                            icon: 'toggle-switch'
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            user_font_size: "20sp"
                                            on_press: root.starting_position()        
                                                
                                    MDCard:
                                        pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                        orientation:"vertical"
                                        size_hint: None, None
                                        size: "150dp", "150dp"
                                        radius:[15]
                                        ripple_behavior: True
                                        FitImage: 
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                                            source: "Spiral patternclear.png"
                                            size_hint: None, None
                                            size: 140, 140
                                    MDBoxLayout:
                                        orientation:"horizontal" 
                                        padding: "60dp"
                                        MDLabel:
                                            id: label
                                            text: "Reversed"
                                            text_color: 1, 1, 1, 1
                                            pos_hint: { "center_x": 0.5, "center_y": 0.5 }
                

            ##lighting icon in bottom nav bar
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Lighting'
                icon: 'flare'
                ##lighting screen
        ''')
        return Navigation()



if __name__ == '__main__':
    Test().run()