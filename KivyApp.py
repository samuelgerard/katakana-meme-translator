import kivy
from kivy.app import App #<----- builds the window and the graphics of the module
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.uix.floatlayout import FloatLayout

from katakana_shitpost_bot import *

App_Version = '1.0.0'

# class Touch(Widget):

# 	btn = ObjectProperty(None)

# 	def on_touch_down(self, touch):
# 		print("")
# 		self.btn.opacity = 0.5

# 	def on_touch_move(self, touch):
# 		print("Mouse Move", touch)

# 	def on_touch_up(self, touch):
# 		print("Mouse Up", touch)
# 		self.btn.opacity = 1

class MyGrid(Widget):
	inputted_text = ObjectProperty(None)
	output_text = ObjectProperty(None)
	katakana_translator = katakana_meme_bot()
	return_string = ""


	def btn(self):
		self.output_text.text = "Now Querying and translating....(Depending on the size of wall it text, the translation can take up to 45-60 seconds)"
		print(f"Inputted_text: {self.inputted_text.text}")
		temp_string = self.inputted_text
		print(f'the string is:{temp_string.text}')
		li = list(temp_string.text.split(" "))
		self.return_string = self.katakana_translator.Activate_shitpost(li)
		

		self.output_text.text = str(" ".join(self.return_string))







# class MyGrid(GridLayout):
# 	def __init__(self, **kwargs):
# 		super(MyGrid, self).__init__(**kwargs)
# 		self.cols = 1

# 		self.inside = GridLayout()
# 		self.inside.cols = 2

# 		self.inside.add_widget(Label(text = "String Input: "))
# 		self.String_Input = TextInput(multiline = False)
# 		self.inside.add_widget(self.String_Input)

# 		self.inside.add_widget(Label(text = "kekw: "))
# 		self.kekw = TextInput(multiline = False)
# 		self.inside.add_widget(self.kekw)


# 		self.submit = Button(text="Submit For Memes", font_size = 40)
# 		self.submit.bind(on_press=self.pressed)
# 		self.add_widget(self.submit)

# 		self.add_widget(self.inside)

# 	def pressed(self, instance):
# 		String_to_be_processed = self.String_Input.text

# 		print(String_to_be_processed)

# 		self.String_Input.text = ""


class MyApp(App):
	def build(self):
		self.title = f"Full Katakana Translator Ver. {App_Version}"
		return MyGrid()

if __name__ == '__main__':
	MyApp().run()