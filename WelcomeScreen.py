from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        welcome_label = Label(text='Добро пожаловать!', font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(welcome_label)
        self.add_widget(layout)
