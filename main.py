from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivy.core.window import Window


class ScreenApp(MDScreen):
    status = 0
    output = "----"
    instructionDisplay = "Enter Decimal number"
    eMesage = ""
    def flip(self):
        if self.status == 0:
            self.status = 1
            self.instructionDisplay = "Enter Binary number"
            self.ids.image.source = "B2D.png"
        else:
            self.status = 0
            self.instructionDisplay = "Enter Decimal number"
            self.ids.image.source = "D2B.png"

    def wipe(self):
        self.ids.number.text = ""

    def convert(self):
        if self.ids.number.text != self.instructionDisplay and self.ids.number.text != "":
            if self.status == 0: #Binary to Decimal
                self.decimal_conv_if_valid()
            elif self.status == 1:    #Decimal to Binary
                self.binary_conv_if_valid()
            self.ids.output_id.text = self.output
        else:
            self.ids.output_id.text = "----"
        self.wipe()

    def default(self):
        self.ids.number.text = self.instructionDisplay

    def decimal_conv_if_valid(self):
        try:
            self.output = bin(int(self.ids.number.text))[2:]
            self.eMesage = ""
            self.ids.eMesage.text = self.eMesage
        except ValueError:
            self.eMesage = "Invalid Number"
            self.ids.eMesage.text = self.eMesage
            self.output = "----"
            self.ids.output_id.text = self.output

    def binary_conv_if_valid(self):
        try:
            self.output = str(int(self.ids.number.text, 2))
            self.eMesage = ""
            self.ids.eMesage.text = self.eMesage
        except ValueError:
            self.eMesage = "Invalid Number"
            self.ids.eMesage.text = self.eMesage
            self.output = "----"
            self.ids.output_id.text = self.output

class MainApp(MDApp):
    def build(self):
        #Window.size = (310, 600)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"

class Card(MDCard):
    pass
class Header(MDToolbar):
    pass
class Input(MDTextField):
    pass
class Button_submit(MDRectangleFlatButton):
    pass

MainApp().run()
