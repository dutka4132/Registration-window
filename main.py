import kivy
kivy.require('1.9.1')
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App

from kivy.core.window import Window
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.image import Image

Builder.load_file('mainwidgets.kv')
Builder.load_file('secondwidgets.kv')
screen = (450, 200)
Window.size = screen
Window.resizable = False


class MainWidgets(Screen):
    """
    The first scene for -sign up-
    """
    def sign_up(self, mail, password): # instance - экземпляр кнопки
        if mail == '':
            self.ids.error.text = 'Firstly input your mail.'
        elif password == '':
            self.ids.error.text = 'Firstly input your password.'
        elif correct_data(self, mail):
            pass
        else:
            user = User(mail, password)

            if not(user is None):
                self.ids.error.text = 'Perfect! Account is registered.'
                self.ids.error.color = (.188, .835, .784, 1)
                self.ids.error.pos_hint = {'center_x': .21, 'center_y': 1}

            else:
                self.ids.error.text = 'This mail is already in use...'
                self.ids.error.color = (1, 1, 0, 1)
                self.ids.error.pos_hint = {'center_x': .21, 'center_y': 1}
                del user

    def sign_in(self): # changing the screen to the -scene of sign in-
        self.manager.current = 'second'


class SecondWidgets(Screen):
    """
    The second scene for -sign in-
    """
    def sign_in(self, mail, password):
        if mail == '':
            self.ids.error.text = "Don't forget input your mail."
        elif password == '':
            self.ids.error.text = "Don't forget input your password."
        elif correct_data(self, mail):
            pass
        elif not(mail in data) or password != data.get(mail):
            self.ids.error.text = "Wrong mail or password."
        else:
            # the screen of app after -sign in- to account
            self.clear_widgets()
            Window.size = (900, 700)
            img = Image(source='bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8 (1).png', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': .5, 'center_y': .5})
            self.add_widget(img)

    def back(self): # changing the screen to the -scene of sign up-
        self.manager.current = 'main'


class AccountRegistrationApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainWidgets(name='main'))
        sm.add_widget(SecondWidgets(name='second'))
        return sm


class User:
    """
    Creating an account and its properties for user
    """
    def __new__(cls, *args, **kwargs):
        if not(args[0] in data): # check of originality of an account
            return super().__new__(cls)

    def __init__(self, mail='', password=''):
        self.mail = mail
        self.password = password
        data[self.mail] = self.password  # add information about user to -data-

    def get_password(self):
        print(self.password)

    def get_mail(self):
        print(self.mail)

    def set_mail(self):
        mail = input('Write another mail: ')

        if not(mail in data):
            print('Perfect! Account is registered')
            self.mail = mail
        else:
            print('This mail is already in use...')
            return self.set_mail()

    def set_new_password(self):
        new_password = input('Write a new password: ')

        while new_password == self.password:
            print("You are't able to use your old password for your new password...")
            new_password = input('Write a new password: ')

        print('The password was update!')
        self.password = new_password
        data[self.mail] = self.password


def correct_data(self, mail): # check of spelling correctness
    if not('@' in mail):
        self.ids.error.text = 'Incorrect mail.'
        self.ids.error.pos_hint = {'center_x': .1, 'center_y': 1}
        return True

    elif len(mail[mail.find('@') + 1:]) <= 4 or len(mail[:mail.find('@')]) == 0:
        self.ids.error.text = 'Incorrect mail.'
        self.ids.error.pos_hint = {'center_x': .1, 'center_y': 1}
        return True

    else:
        return False


data = {} # data of users

# users
nikita = User('table@gmail.com', '12345')
artur = User('table@gmail.com', '1000')
klim = User('chair@mail.ru', '0000')

if __name__ == '__main__':
    AccountRegistrationApp().run()
