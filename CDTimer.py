# CountDown Timer (v1.0 / WIP)
# Original Author: Brokenshire@GitHub (https://github.com/Brokenshire)
# Modifications and slight adaptations: TheDigitalJoker (https://github.com/thedigitaljoker)
# Quote of the day: "Only the dead have seen the end of the War" - Plato

from tkinter import *
import time
import tkinter.messagebox

# == Defining the countdown function and functional buttons ==
class Countdown:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.running = False
        self.time1 = ''
        self.prevSec = ''
        self.mins = 0 # changed from 10 to 0
        self.secs = 0
        self.hours = 0

        self.clock = Label(frame, width=7, font=('fixed', 20))
        self.clock.grid(row=1, columnspan=9, padx=5, pady=(5, 2))
        self.tick()

        self.plusButton = Button(frame, text="+", command=self.pluscountdown)
        self.plusButton.grid(row=2, column=1)

        self.minusButton = Button(frame, text="-", command=self.minuscountdown)
        self.minusButton.grid(row=2, column=2)

        self.startButton = Button(frame, text="Start", command=self.startcountdown)
        self.startButton.grid(row=2, column=3)

        self.stopButton = Button(frame, text="Stop", command=self.stopcountdown, state="disabled")
        self.stopButton.grid(row=2, column=4)

        self.resetButton = Button(frame, text="Reset", command=self.resetcountdown, state="disabled")
        self.resetButton.grid(row=2, column=5)

        self.quitButton = Button(frame, text="Exit", command=self.quitcountdown)
        self.quitButton.grid(row=2, column=6)

    def tick(self):
        if self.running == True:
            self.newSec = time.strftime('%H:%M:%S')
        else:
            self.newSec = ''
            self.prevSec = ''
        if self.newSec != self.prevSec:
            self.prevSec = self.newSec
            self.secs = self.secs - 1
            if self.secs < 0:
                self.secs = 59
                self.mins = self.mins - 1
                if self.mins < 0:
                    self.mins = 59
                    self.hours = self.hours - 1
                    if self.hours < 0:
                        self.hours = 0
                        self.mins = 0
                        self.secs = 0
                        self.plusButton.config(state="normal")
                        self.minusButton.config(state="normal")
                        self.startButton.config(state="normal")
                        self.stopButton.config(state="disabled")
                        self.resetButton.config(state="normal")
                        self.quitButton.config(state="normal")
        self.time2 = ('%02d:%02d:%02d' % (self.hours, self.mins, self.secs))
        if self.time2 != self.time1:
            self.time1 = self.time2
            self.clock.config(text=self.time2)
        self.clock.after(200, self.tick)

    def pluscountdown(self):
        self.mins = self.mins + 1
        if self.secs > 60:
            self.secs = 0
            self.mins = self.mins + 1
            if self.mins > 60:
                self.mins = 0
                self.hours = self.hours + 1
                if self.hours > 60:
                    self.hours = 0
                    self.mins = 0
                    self.secs = 0
        self.resetButton.config(state="normal")

    def minuscountdown(self):
        self.mins = self.mins - 1
        if self.secs < 0:
            self.secs = 60
            self.mins = self.mins - 1
            if self.mins < 0:
                self.mins = 60
                self.hours = self.hours - 1
                if self.hours < 0:
                    self.hours = 0
                    self.mins = 0
                    self.secs = 0
        self.resetButton.config(state="normal")

    def startcountdown(self):
        self.running = True
        self.plusButton.config(state="disabled")
        self.minusButton.config(state="disabled")
        self.startButton.config(state="disabled")
        self.stopButton.config(state="normal")
        self.resetButton.config(state="disabled")
        self.quitButton.config(state="disabled")

    def stopcountdown(self):
        self.running = False
        self.plusButton.config(state="normal")
        self.minusButton.config(state="normal")
        self.startButton.config(state="normal")
        self.stopButton.config(state="disabled")
        self.resetButton.config(state="normal")
        self.quitButton.config(state="normal")

    def resetcountdown(self):
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.prevSec = ''
        self.time1 = ''
        self.running = False
        self.plusButton.config(state="normal")
        self.minusButton.config(state="normal")
        self.startButton.config(state="normal")
        self.stopButton.config(state="disabled")
        self.resetButton.config(state="disabled")
        self.quitButton.config(state="normal")
	
    def quitcountdown(self):
        self.mExit = tkinter.messagebox.askokcancel(title="CountDownTimer", message="I know you're sure you want to exit so I'll just wish you a nice day!")
        print(self.mExit)
        if self.mExit > 0:
            root.destroy()
            return

# == Setting up the root window and its attributes ==
root = Tk()
root.title("CDTimer") # Modified from TK's default "Scoreboard"
c = Countdown(root)
w = 200 # root window width
h = 80 # root window height

# get screen width and height
ws = root.winfo_screenwidth() # screen width 
hs = root.winfo_screenheight() # screen height

# calculate x and y coordinates for the root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# setting up the default root window opening position 
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#root.geometry("200x80+0+0") - disabled functionality, it was opening the window in the top left corner
root.resizable(0, 0) # makes root window not resizable in the x/y directions
root.mainloop()
