__doc__="""
This is the first basic kivy app
https://kivy.org/doc/stable/guide/basic.html#quickstart
"""

import kivy
# kivy.require('x.x.x') # replace with your current kivy version!

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

class MyApp(App):
    title = "BasicApp"
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Hello, world!")
        btn1 = Button(text = "button (1)")
        btn2 = Button(text = "button (2)")
        sld = Slider(max=10, min=0, value=2)
        layout.add_widget(label)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(sld)
        return layout

if __name__ == "__main__":
    app = MyApp()
    app.run()

