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
    pass

class Test(MDApp): 
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
                    
                    MDFloatLayout:
                        MDIconButton:
                            icon: "repeat"
                            user_font_size: "40sp"
                            pos: 555, 300
                    
                    MDFloatLayout:
                        MDLabel:
                            text: "Shuffle on"
                            font_size: "10sp"
                            pos: 865, 280
                        MDIconButton:
                            icon: "shuffle"
                            user_font_size: "40sp"
                            pos: 855, 300
                            
            ##Middle playlist icon in navigation bar
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Plalists'
                icon: 'playlist-plus'
                ##Playlist screen

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