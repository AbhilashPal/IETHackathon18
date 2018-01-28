import tkinter
import tkinter.messagebox
def func3():    
	window = tkinter.Tk()
	window.geometry('400x400'.format(500, 500))
	window.configure(background = '#a1dbcd')
	window.title("Fake News?")

	#photo
	photo = tkinter.PhotoImage(file = 'sentdex-long-banner-dark.png')
	w = tkinter.Label(window, image = photo)
	w.pack()

	#label for instructions
	lblInst = tkinter.Label(window, text = "Perform a Quick Analysis!", fg = '#383a39', bg = '#a1dbcd', font = ("Helvetica", 16))
	lblInst.pack()

	#for entering username
	def retrieve_input():
		inputvalue = textBox.get("1.0", "end-1c")	
		import main
		main.run(inputvalue)
	lbluser = tkinter.Label(window, text = "Enter a Query", fg = '#383a39', bg = '#a1dbcd')
	textBox = tkinter.Text(window, height = 2, width = 10)
	btn = tkinter.Button(window, text = "Let's GO!", bg = '#383a39', fg = '#a1dbcd', command = lambda: retrieve_input())
	btn.pack()
	lbluser.pack()
	textBox.pack()
	window.mainloop()

if __name__ == '__main__':
	func3()