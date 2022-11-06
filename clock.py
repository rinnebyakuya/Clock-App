from tkinter import *
from time import *

def update():                                                                       # a recursive function to update the values in the window every 1000 ms  
    time_string = strftime("%I:%M:%S %p")                                           # get the current time using strftime from time library
    time_label.config(text = time_string)                                           # set the time_label text to the time_string

    day_string = strftime("%A")                                                     # repeat fo other labels
    day_label.config(text = day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text = date_string)

    window.after(1000, update)                                                      # call the function recursively after 1000ms

 
window = Tk()                                                                       # the window where we show the lables

w = 800 
h = 320 
window.config(bg='Black')                                                           # set up the background to black
window.resizable(width = False, height = False)                                     # and the resizability to false
ws = window.winfo_screenwidth()                                                     # get the width of the screen
hs = window.winfo_screenheight()                                                    # get the height of the screen

x = (ws/2) - (w/2)                                                                  # calculate x new position
y = (hs/2) - (h/2)                                                                  # calculate y new position

window.geometry('%dx%d+%d+%d' % (w, h, x, y))                                       # set the psotion and the size of the window

name_label = Label(window, font = ("Arial",50), fg = "#00FF00", bg = "Black")       # show the name of the program
name_label.config(text = "A Simple Digital Clock")
name_label.pack()

time_label = Label(window, font = ("Arial",50), fg = "#00FF00", bg = "Black")       # show the time
time_label.pack()

day_label = Label(window, font = ("Arial",50), fg = "#00FF00", bg = "Black")        # show the day
day_label.pack()

date_label = Label(window, font = ("Arial",50), fg = "#00FF00", bg = "Black")       # show the date
date_label.pack()

update()                                                                            # calling our update function
window.mainloop()