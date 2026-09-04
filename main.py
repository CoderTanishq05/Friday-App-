from kivy.app import App
from kivy.uix.button import Button

class FridayApp(App):
    def build(self):
        return Button(text="FRIDAY is Alive! Jarvis Mode", font_size=24)

FridayApp().run()