from kivy.core.window import Window

Window.clearcolor = (0.5, 1, 0.5, 1)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import RegistrationScreen, WelcomeScreen, LoginScreen


class RegistrationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(LoginScreen(name='login'))  # Добавление экрана входа
        sm.add_widget(WelcomeScreen(name='welcome'))
        return sm


if __name__ == "__main__":
    RegistrationApp().run()
