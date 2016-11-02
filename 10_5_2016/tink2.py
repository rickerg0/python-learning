from Tkinter import *

def say_hi():
        print "hi there, everyone!"
        
root = Tk()

frame = Frame(root)
frame.pack()

button = Button (frame, text="QUIT", fg="red", command=frame.quit )
button.pack(side=LEFT)

hi_there = Button(frame, text="Hello", command=say_hi)
hi_there.pack(side=LEFT)


root.mainloop()
root.destroy() # optional; see description below
