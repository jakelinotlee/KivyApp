from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from kivy.core.window import Window
import random

Window.clearcolor = (255/255.0, 155/255.0, 128/255.0, 1)
LabelBase.register(name= "Pacifico",
                   fn_regular= "Pacifico.ttf")


class IntroWindow(Screen):
    pass


class MainWindow(Screen):
    itemList = ObjectProperty(None)

    def choose(self, **kwargs):
        input_items = self.itemList.text
        item_list = input_items.split(",")
        chosen_one = random.choice(item_list)
        PopupWindow = ChoosePopup(chosen_one)
        print(chosen_one)
        PopupWindow.open()


class ChoosePopup(Popup):
    chosen_item = StringProperty()

    def __init__(self, chosen_one, **kwargs):
        super(ChoosePopup, self).__init__(**kwargs)
        self.chosen_item = chosen_one


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
