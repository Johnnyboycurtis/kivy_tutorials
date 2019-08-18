__doc__="""
This is the first basic kivy app
https://kivy.org/doc/stable/guide/basic.html#quickstart
"""

import kivy
kivy.require('1.0.9')
# kivy.require('x.x.x') # replace with your current kivy version!

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider


def some_action(instance):
    print("Button {} was pressed".format(instance.text))

def show_value(instance, other):
    print("Value: {}".format(instance.value))
    print(type(instance), type(other))

class MyApp(App):
    title = "BasicApp"
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Hello, world!")
        btn1 = Button(text = "Button A", font_size = 18)
        btn1.bind(on_press = some_action)
        btn2 = Button(text = "Button B")
        sld = Slider(max=10, min=0, value=2)
        sld.bind(on_touch_move = show_value) # on_touch_
        layout.add_widget(label)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(sld)
        return layout

if __name__ == "__main__":
    app = MyApp()
    app.run()

