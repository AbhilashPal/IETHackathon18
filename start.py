def func2():
	import tkinter
	import tkinter.messagebox
	def create_window():
	    win = tkinter.Toplevel(window)

	    
	window = tkinter.Tk()
	window.configure(background = '#a1dbcd')
	window.title("Fake News?")

	#photo
	photo = tkinter.PhotoImage(file = 'sentdex-long-banner-dark.png')
	w = tkinter.Label(window, image = photo)
	w.pack()

	#label for instructions
	lblInst = tkinter.Label(window, text = "Perform a quick Fake News Analysis", fg = '#383a39', bg = '#a1dbcd', font = ("Helvetica", 16))
	lblInst.pack()

	#for entering username
	lbluser = tkinter.Label(window, text = "Search on Facebook", fg = '#383a39', bg = '#a1dbcd')
	entuser = tkinter.Entry(window)
	btn = tkinter.Button(window, text = "Let's GO!", bg = '#383a39', fg = '#a1dbcd', command = create_window)
	lbluser.pack()
	entuser.pack()
	btn.pack()

	#for wntering password
	lblpass = tkinter.Label(window, text = "Search on Twitter", fg = '#383a39', bg = '#a1dbcd')
	entpass = tkinter.Entry(window)
	btn = tkinter.Button(window, text = "Let's GO!", bg = '#383a39', fg = '#a1dbcd')
	lblpass.pack()
	entpass.pack()
	btn.pack()
	window.mainloop()

if __name__ == '__main__':
	func2()