from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (480, 640)


class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Amber"
        return Builder.load_file("calc.kv")

    def update_input(self, value):
        self.root.ids.input_field.text += value

    def clear_input(self):
        self.root.ids.input_field.text = ""

    def backspace(self):
        current_text = self.root.ids.input_field.text
        self.root.ids.input_field.text = current_text[:-1]

    def calculate(self):
        try:
            expression = self.root.ids.input_field.text
            result = str(eval(expression))
            self.root.ids.input_field.text = result
        except Exception as e:
            self.root.ids.input_field.text = "На ноль делить нельзя!"


if __name__ == '__main__':
    CalculatorApp().run()