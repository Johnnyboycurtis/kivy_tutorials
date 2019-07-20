from kivy.app import App
from kivy.uix.gridlayout import GridLayout # similar to slicers in wxpython
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        username_label = Label(text = "Username: ")
        self.add_widget(username_label)
        username_input = TextInput(text = 'Enter Username', multiline=False) # do you have to append it to self??
        self.add_widget(username_input)
        
        password_label = Label(text = "Password: ")
        self.add_widget(password_label)
        password_input = TextInput(text = "Enter Password", multiline=False)
        self.add_widget(password_input)


class MyApp(App):
    title = "Login Screen"

    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    app = MyApp()
    app.run()


