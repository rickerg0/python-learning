from Tkinter import *

class SlotMachine:
    slot1 = Label
    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.bet = Button(frame, text="Bet", command=self.bet)
        self.bet.pack(side=LEFT)

        self.gamble = Button(frame, text="Gamble", command=self.gamble)
        self.gamble.pack(side=LEFT)

        self.sf = Frame(master,borderwidth=20)
        self.slot1 = Label(self.sf,bg="red" ,text="slot 1",height=10,width=10,borderwidth=5)
        self.slot1.grid( row=0, column=0 )
        
        self.slot2 = Label(self.sf,bg="pink" , text="slot 2",height=10,width=10,borderwidth=5)
        self.slot2.grid( row=0, column=1 )
        self.slot3 = Label(self.sf,bg="green" , text="slot 3",height=10,width=10,borderwidth=5)
        self.slot3.grid( row=0, column=2 )
        self.sf.pack()

    def bet(self):
        print "hi there, everyone!"
        
    def gamble(self):
        self.slot1.configure(bg='yellow')
        self.slot2.configure(bg='red')
        self.slot3.configure(bg='blue')
        self.sf.update()
