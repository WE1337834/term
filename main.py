from kivy.core.window import Window

Window.clearcolor = (0, 0.2196, 0.2784, 1)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import *


class RegistrationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Auth(name="auth"))
        sm.add_widget(BuyTokenScreen(name="buytoken"))
        # sm.add_widget(RegistrationScreen(name='registration'))
        # sm.add_widget(LoginScreen(name='login'))
        # sm.add_widget(WelcomeScreen(name='welcome'))
        return sm


if __name__ == "__main__":
    RegistrationApp().run()
