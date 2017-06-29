from Tkinter import *

class Application(Frame):

	def __init__(self, master):
		'Initialize the Frame'
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):

		# Title label
		self.instruction = Label(self, text = "PyCaesar",
			font = ("Monaco", 17, "bold"))
		self.instruction.grid(row = 1, column = 0,
			columnspan = 2, padx = 5, sticky = W)

		# Method label
		self.method = Label(self, text = "Choose method:")
		self.method.grid(row = 2, column = 0,
			columnspan = 2, padx = 5, sticky = W)

		# Method options
		self.var1 = IntVar()
		self.option = Radiobutton(self, text = "Encrypt", pady = 5,
			variable = self.var1, value = 1)
		self.option.grid(row = 3, column = 0, columnspan = 1, padx = 5, sticky = W)


		self.option = Radiobutton(self, text = "Decrypt", pady = 5,
			variable = self.var1, value = 2)
		self.option.grid(row = 3, column = 1, columnspan = 1, padx = 5, sticky = W)

		# Message label
		self.instruction = Label(self, text = "Enter message: ")
		self.instruction.grid(row = 4, column = 0,
			columnspan = 150, padx = 5, sticky = W)

		# Message entry
		self.message = Entry(self)
		self.message.grid(row = 5, column = 0, padx = 5, sticky = W)

		# Key label
		self.instruction = Label(self, text = "Enter key (1-26):")
		self.instruction.grid(row = 6, column = 0,
			columnspan = 2, padx = 5, sticky = W)

		# Key entry
		self.key = Entry(self)
		self.key.grid(row = 7, column = 0, padx = 5, sticky = W)

		# Submit
		self.submit_button = Button(self, text = "Submit", command = self.caesar)
		self.submit_button.grid(row = 8, column = 0, padx = 5, sticky = W)

		# Result label
		self.instruction = Label(self, text = "Result", font=("Monaco", 14, "bold"))
		self.instruction.grid(row = 9, column = 0,
			columnspan = 2, padx = 5, sticky = W)

		# Result
		self.result = Text(self, width = 45, height = 6, wrap = WORD)
		self.result.grid(row = 10, column = 0,
			columnspan = 3, padx = 5, sticky = W)

	def caesar(self):
		m = self.message.get()
		k = int(self.key.get())
		if (self.var1.get()) == 2:
			k = -k
		ciphertext = ''
		for character in m:
			if character.isalpha():
				num = ord(character) + k

				if character.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26

				elif character.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26

				ciphertext += chr(num)
			else:
				ciphertext += character

		self.result.delete(0.0, END)
		self.option.deselect()
		self.result.insert(0.0, ciphertext)

		return ciphertext

root = Tk()
root.title("PythonCaesar")
root.geometry("330x350")
app = Application(root)
root.mainloop()