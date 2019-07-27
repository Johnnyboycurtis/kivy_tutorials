import kivy
# kivy.require('x.x.x') # replace with your current kivy version!
kivy.require('1.0.9')
# if you do not  know what version to enter
# consider printing kivy.__version__
# this will ensure apps run in the version used to build the app

from kivy.app import App # base class for creating Kivy apps
from kivy.uix.label import Label # a label widget

class helloApp(App):
    """
    Since this app is called `helloApp` the kivy language file
    should be called hello.kv
    Reference: https://kivy.org/doc/stable/guide/lang.html
    """

    def build(self):
        return Label()

if __name__ == "__main__":
    app = helloApp()
    app.run()

r