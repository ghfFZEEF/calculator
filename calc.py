from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class CalculatorApp(App):
    def __init__(self):
        super().__init__()
        self.lbl = Label(text='0',
                         font_size=40,
                         size_hint=(1, .3),
                         halign='right',
                         valign='center',
                         text_size=(350, 500 * .4 - 50))
        self.back = None
        self.zn = None

    def build(self):

        bl = BoxLayout(orientation='vertical', spacing=3)
        gl = GridLayout(cols=4, padding=5, spacing=3, size_hint=(1, .7))

        gl.add_widget(Button(text=f'CE', on_press=self.ne_zn))
        gl.add_widget(Button(text=f'C', on_press=self.ne_zn))
        gl.add_widget(Button(text=f'back', on_press=self.ne_zn))
        gl.add_widget(Button(text=f'/', on_press=self.for_zn))

        gl.add_widget(Button(text=f'7', on_press=self.add_num))
        gl.add_widget(Button(text=f'8', on_press=self.add_num))
        gl.add_widget(Button(text=f'9', on_press=self.add_num))
        gl.add_widget(Button(text=f'*', on_press=self.for_zn))

        gl.add_widget(Button(text=f'4', on_press=self.add_num))
        gl.add_widget(Button(text=f'5', on_press=self.add_num))
        gl.add_widget(Button(text=f'6', on_press=self.add_num))
        gl.add_widget(Button(text=f'-', on_press=self.for_zn))

        gl.add_widget(Button(text=f'1', on_press=self.add_num))
        gl.add_widget(Button(text=f'2', on_press=self.add_num))
        gl.add_widget(Button(text=f'3', on_press=self.add_num))
        gl.add_widget(Button(text=f'+', on_press=self.for_zn))

        gl.add_widget(Button(text=f'+/-', on_press=self.ne_zn))
        gl.add_widget(Button(text=f'0', on_press=self.add_num))
        gl.add_widget(Button(text=f'.', on_press=self.add_t))
        gl.add_widget(Button(text=f'=', on_press=self.ne_zn))

        bl.add_widget(self.lbl)
        bl.add_widget(gl)

        return bl

    def add_num(self, instance):
        if self.lbl.text == self.back:
            self.lbl.text = '0'
        if self.lbl.text == '0':
            self.lbl.text = str(instance.text)
        else:
            self.lbl.text += str(instance.text)

    def for_zn(self, instance):
        if self.back is not None:
            vl = str(eval(f'{float(self.back)} {self.zn} {float(self.lbl.text)}'))
            if float(vl).is_integer():
                self.lbl.text = str(int(float(vl)))
            else:
                self.lbl.text = vl
            self.back = self.lbl.text
            self.zn = instance.text
        else:
            self.back = self.lbl.text
            self.zn = instance.text
            self.lbl.text = '0'

    def add_t(self, instance):
        if instance.text not in self.lbl.text:
            self.lbl.text += instance.text

    def ne_zn(self, instance):
        if instance.text == '=':
            if self.back is not None:
                vl = str(eval(f'{float(self.back)} {self.zn} {float(self.lbl.text)}'))
                if float(vl).is_integer():
                    self.lbl.text = str(int(float(vl)))
                else:
                    self.lbl.text = vl
                self.back = None
            else:
                self.lbl.text = self.lbl.text

        elif instance.text == 'CE':
            self.lbl.text = '0'
            self.back = None
            self.zn = None

        elif instance.text == 'C':
            self.lbl.text = '0'

        elif instance.text == 'back':
            self.lbl.text = self.lbl.text[:-1]

        elif instance.text == '+/-':
            if self.lbl.text[0] == '-':
                self.lbl.text = self.lbl.text[1:]
            else:
                self.lbl.text = '-' + self.lbl.text


if __name__ == '__main__':
    CalculatorApp().run()
