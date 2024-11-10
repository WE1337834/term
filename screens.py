from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from database import insert_data, check_credentials


class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        self.label_name = Label(text='Логин', color=(0, 0, 1, 1), font_size=20,
                                pos_hint={'center_x': 0.5, 'center_y': 0.75})
        self.inp_name = TextInput(multiline=False, size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.7})

        self.label_pass = Label(text='Пароль', color=(0, 0, 1, 1), font_size=20,
                                pos_hint={'center_x': 0.5, 'center_y': 0.65})
        self.inp_pass = TextInput(multiline=False, password=True, size_hint=(0.4, 0.05),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.6})

        btn_register = Button(text="Зарегистрироваться", background_color=(0, 1, 0, 1), size_hint=(0.4, 0.06),
                              font_size=20, pos_hint={'center_x': 0.5, 'center_y': 0.4})
        btn_register.bind(on_press=self.register_user)

        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint=(0.4, 0.05),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.35})

        btn_to_login = Button(text='Перейти на экран входа', size_hint=(0.4, 0.06),
                              pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_to_login.bind(on_press=self.go_to_login)

        layout.add_widget(self.label_name)
        layout.add_widget(self.inp_name)
        layout.add_widget(self.label_pass)
        layout.add_widget(self.inp_pass)
        layout.add_widget(btn_register)
        layout.add_widget(self.error_label)
        layout.add_widget(btn_to_login)

        self.add_widget(layout)

    def register_user(self, instance):
        name = self.inp_name.text.strip()
        password = self.inp_pass.text.strip()

        if name and password:
            if insert_data(name, password):  # Предполагается, что insert_data возвращает True при успешной регистрации
                print("Регистрация успешна!")
                self.manager.current = 'login'  # Переключение на экран входа
            else:
                self.error_label.text = "Ошибка регистрации!"  # Отображение сообщения об ошибке
        else:
            self.error_label.text = "Пожалуйста, заполните все поля!"  # Проверка на пустые поля

    def go_to_login(self, instance):
        self.manager.current = 'login'  # Переключение на экран входа


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        welcome_label = Label(text='Добро пожаловать!', font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(welcome_label)
        self.add_widget(layout)


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout(size=(20, 20))

        headliner = Label(text='Вход', color=(0, 0, 0, 1), size_hint=(0.4, 0.05), font_size=20,
                          pos_hint={'center_x': 0.5, 'center_y': 0.945})

        self.label_name = Label(text='Логин', color=(0, 0, 1, 1), font_size=20,
                                pos_hint={'center_x': 0.5, 'center_y': 0.76})
        self.inp_name = TextInput(multiline=False, size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.71})

        self.label_pass = Label(text='Пароль', color=(0, 0, 1, 1), font_size=20,
                                pos_hint={'center_x': 0.5, 'center_y': 0.66})
        self.inp_pass = TextInput(multiline=False, password=True, size_hint=(0.4, 0.05),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.61})

        btn = Button(text="Войти", background_color=(0, 1, 0, 1), size_hint=(0.4, 0.06), font_size=20,
                     pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn.bind(on_press=self.login_user)

        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint=(0.4, 0.05),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.25})

        self.layout.add_widget(headliner)
        self.layout.add_widget(self.label_name)
        self.layout.add_widget(self.inp_name)
        self.layout.add_widget(self.label_pass)
        self.layout.add_widget(self.inp_pass)
        self.layout.add_widget(btn)
        self.layout.add_widget(self.error_label)  # Добавление метки для ошибок

        self.add_widget(self.layout)

    def login_user(self, instance):
        name = self.inp_name.text.strip()
        password = self.inp_pass.text.strip()

        if check_credentials(name, password):
            print("Успешный вход!")
            self.manager.current = 'welcome'  # Переключение на экран приветствия
        else:
            self.error_label.text = "Неверный логин или пароль!"  # Отображение сообщения об ошибке
