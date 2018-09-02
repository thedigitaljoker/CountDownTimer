# CountDownTimer (v1.0 / WIP)

Original author: [Brokenshire](https://github.com/Brokenshire)

Modifications and slight adaptations: TheDigitalJoker

Dependencies: Python 2.7

Tested on: Python 2.7.15 / Windows 7 (Ultimate, x64 version)

# Modifications/adaptations
1. Changed default countdown minutes (self.mins = ) from 10 to 0.
2. Changed root window close buttons name from "Quit" to "Exit".
3. Changed root window title to "CDTimer".
4. Changed root window default opening size from top left corner to the screen's center using xxmbabanexx's answer on a [StackOverflow topic](https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens).
5. Changed the exit message to a funny one.
6. Added an audio and visual user notification, using the winsound module and tkinter's messagebox.showinfo's package.

# To do
1. ~~Add an audio and/or visual user notification when the set time has occured.~~ *Half fixed, for now it only works on Windows since it uses the winsound module. Need to think of a method to play a specific sound and insert it into the compiled PE file.*
2. Extend functionality with preset timers (30, 60, 90 minutes).
3. Change the default value for increasing/decreasing the timer from 1 minute to 5 minutes (optional).
4. Change the root window's icon from the default Tk to an appropriate one.
5. Compile a PE file (for Windows and Linux at least) for users with no Python installed. 
