from SlotMachine import SlotMachine

from Tkinter import *

        
root = Tk()
frame = Frame(root,height=400,width=800)
frame.pack()
app = SlotMachine(frame)


root.mainloop()
root.destroy() 
