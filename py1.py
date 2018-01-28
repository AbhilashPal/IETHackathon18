import tkinter
def func1():
    

    root1 = tkinter.Tk()
    root1.title("Fake News?")
    photo = tkinter.PhotoImage(file = 'sentdex-long-banner-dark.png')
    w = tkinter.Label(root1, image = photo)
    w.pack()

    def kill1():
        root1.destroy()
        from start1 import func3
        func3()
    def kill2():
        root1.destroy()
        from start import func2
        func2()

    button1 = tkinter.Button(root1, text = 'Perform a quick Fake News Analysis', command = kill1, fg = '#383a39', bg = '#a1dbcd', font = ("Helvetica", 16), padx = 20, pady = 20)
    button1.pack()
    button1 = tkinter.Button(root1, text = 'Scourge the Social Media!', command = kill2, fg = '#383a39', bg = '#a1dbcd', font = ("Helvetica", 16), padx = 20, pady = 20)
    button1.pack()

    root1.mainloop()

