__doc__="""
This is the first basic kivy app
https://kivy.org/doc/stable/guide/basic.html#quickstart
"""

import kivy

# kivy.require('x.x.x') # replace with your current kivy version!

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text = "Hello, world!")

if __name__ == "__main__":
    app = MyApp()
    app.run()

