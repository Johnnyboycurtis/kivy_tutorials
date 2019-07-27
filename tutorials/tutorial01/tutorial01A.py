import kivy
# kivy.require('x.x.x') # replace with your current kivy version!
kivy.require('1.0.9')
# if you do not  know what version to enter
# consider printing kivy.__version__
# this will ensure apps run in the version used to build the app

from kivy.app import App # base class for creating Kivy apps
from kivy.uix.label import Label # a label widget

class MyApp(App):

    def build(self):
        return Label(text = "Hello, world!")

if __name__ == "__main__":
    app = MyApp()
    app.run()

"""
For basic apps like above we can rely on pre-built widgets like Label
However, as apps become more complex, you will want to customize those Labels
and/or create your own Widgets.

You can use the kivy language (or kv language) to build complex widgets
and customize the appearance of your app
"""