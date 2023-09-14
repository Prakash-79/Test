import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')

class Test(App):
    def build(self):
        label = Label(text="Hello World")
        return label
    
if __name__ == "__main__":
    Test().run()