from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from database import insert_data, check_credentials


class Auth(Screen):

    ################## COMPONENTS ##################
    def create_BTN(self, text, size_hint, x, y):
        return Button(
            text=text,
            background_color=(0.10196, 0.2039, 0.2353, 1),
            size_hint=size_hint,
            font_size=20,
            pos_hint={"center_x": x, "center_y": y},
            color=(0.7451, 0.7529, 0.5157, 1),
        )

    def create_INP(self, text, x, y):
        return TextInput(
            text=text,
            multiline=False,
            size_hint=(0.4, 0.05),
            pos_hint={"center_x": x, "center_y": y},
            foreground_color=(0.5, 0.5, 0.5, 1),
        )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()

        self.error_label = Label(
            text="",
            color=(1, 0, 0, 1),
            size_hint=(0.4, 0.05),
            pos_hint={"center_x": 0.5, "center_y": 0.35},
        )
        self.header_login = self.create_BTN("Вход", (0.2, 0.01), 0.35, 0.8)
        # Button(text='Вход', background_color=(0, 0, 0, 0),
        #    size_hint=(0.2, 0.05), font_size=20,
        #    pos_hint={'center_x': 0.35, 'center_y': 0.8})
        self.header_login.bind(on_press=self.login)
        self.header_reg = self.create_BTN("Регистрация", (0.2, 0.01), 0.65, 0.8)

        self.header_reg.bind(on_press=self.reg)

        self.layout.add_widget(self.header_login)
        self.layout.add_widget(self.header_reg)  # Only add this once
        self.layout.add_widget(self.error_label)
        self.add_widget(self.layout)

    def login(self, instance):
        self.login_u = self.create_INP("Введите логин", 0.5, 0.6)
        self.login_u.bind(focus=self.on_focus_name)

        self.pass_u = self.create_INP("Введите пароль", 0.5, 0.5)
        self.pass_u.bind(focus=self.on_focus_pass)
        self.btn = self.create_BTN("Войти", (0.4, 0.06), 0.5, 0.3)
        self.btn.bind(on_press=self.login_user)
        self.layout.add_widget(self.login_u)
        self.layout.add_widget(self.pass_u)
        self.layout.add_widget(self.btn)

    def login_user(self, instance):
        self.name = self.login_u.text.strip()  # Получаем логин
        password = self.pass_u.text.strip()  # Получаем пароль в отдельной переменной

        print(f"Attempting to log in with username: {self.name} and password: {password}")

        if check_credentials(self.name, password):
            print("Успешный вход!")
            self.manager.current = "buytoken"
        else:
            print("Login failed.")
            self.error_label.text = "Неверный логин или пароль!"



    def reg(self, instance):

        self.name_u = self.create_INP("Придумайте логин", 0.5, 0.6)
        self.name_u.bind(focus=self.on_focus_name)

        self.pass_r = self.create_INP("Придумайте пароль", 0.5, 0.5)
        self.pass_r.bind(focus=self.on_focus_pass)
        self.btn = self.create_BTN("Зарегистрироваться", (0.4, 0.06), 0.5, 0.3)
        self.btn.bind(on_press=self.register_user)
        self.layout.add_widget(self.name_u)
        self.layout.add_widget(self.pass_r)
        self.layout.add_widget(self.btn)

    def register_user(self, instance):
        name = self.name_u.text.strip()
        password = self.pass_r.text.strip()

        print(f"Attempting to register with username: {name} and password: {password}")

        if name and password:
            if insert_data(name, password):
                print("Регистрация успешна!")
                self.manager.current = "buytoken"
            else:
                print("Registration failed. User may already exist.")
                self.error_label.text = "Ошибка регистрации!"
        else:
            print("Registration failed. Fields are empty.")
            self.error_label.text = "Пожалуйста, заполните все поля!"

    def on_focus_name(self, instance, value):
        if value:  # Когда фокус установлен
            if hasattr(self, "login_u") and self.login_u.text == "Введите логин":
                self.login_u.text = ""
                self.login_u.foreground_color = (0, 0, 0, 1)  # Черный цвет текста
            if hasattr(self, "name_u") and self.name_u.text == "Придумайте логин":
                self.name_u.text = ""
                self.name_u.foreground_color = (0, 0, 0, 1)  # Черный цвет текста
        else:  # Когда фокус потерян
            if hasattr(self, "login_u") and self.login_u.text == "":
                self.login_u.text = "Введите логин"
                self.login_u.foreground_color = (0.5, 0.5, 0.5, 1)  # Серый цвет текста
            if hasattr(self, "name_u") and self.name_u.text == "":
                self.name_u.text = "Придумайте логин"
                self.name_u.foreground_color = (0.5, 0.5, 0.5, 1)  # Серый цвет текста

    def on_focus_pass(self, instance, value):
        if value:  # Когда фокус установлен
            if hasattr(self, "pass_u") and self.pass_u.text == "Введите логин":
                self.pass_u.text = ""
                self.pass_u.foreground_color = (0, 0, 0, 1)  # Черный цвет текста
            if hasattr(self, "pass_r") and self.pass_r == "Придумайте пароль":
                self.pass_r.text = ""
                self.pass_r.foreground_color = (0, 0, 0, 1)  # Черный цвет текста
        else:  # Когда фокус потерян
            if hasattr(self, "pass_u") and isinstance(self.pass_u, TextInput) and self.pass_u.text == "":
                self.pass_u.text = "Введите пароль"
                self.pass_u.foreground_color = (0.5, 0.5, 0.5, 1)  # Серый цвет текста
                
            if hasattr(self, "pass_r") and isinstance(self.pass_r, TextInput) and self.pass_r.text == "":
                self.pass_r.text = "Придумайте пароль"
                self.pass_r.foreground_color = (0.5, 0.5, 0.5, 1)  # Серый цвет текста



class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        welcome_label = Label(
            text="Добро пожаловать!",
            font_size=30,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        layout.add_widget(welcome_label)
        self.add_widget(layout)


class BuyTokenScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        buying = Label(
            text="Подписаться",
            font_size=30,
            pos_hint={"center_x": 0.5, "center_y": 0.9},
        )
        layout.add_widget(buying)
        self.add_widget(layout)
