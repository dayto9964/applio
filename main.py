from kivy.app import App
from kivy.uix.label import Label

class ApplioApp(App):
    def build(self):
        return Label(text='Applio Mobile')

if __name__ == '__main__':
    ApplioApp().run()
