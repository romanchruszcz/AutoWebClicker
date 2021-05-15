from tkinter import *
import time
import pyautogui

def selected_left():
    HiddenLabel.configure(text="LEFT")

def selected_right():
   HiddenLabel.configure(text="RIGHT")

def selected_middle():
    HiddenLabel.configure(text="MIDDLE")

def manual():
    WidthEntry.config(state=NORMAL)
    WidthEntry.delete(0,"end")
    WidthEntry.insert(0,"width")
    HeightEntry.config(state=NORMAL)
    HeightEntry.delete(0,"end")
    HeightEntry.insert(1,"height")
    WidthEntry.focus()

def auto():
    WidthEntry.configure(state=DISABLED)
    HeightEntry.configure(state=DISABLED)
    NumClicks.focus()


def reset_command():
    HeightEntry.configure(state=NORMAL)
    WidthEntry.configure(state=NORMAL)
    WidthEntry.delete(0,"end")
    HeightEntry.delete(0,"end")
    NumClicks.delete(0,"end")
    Interval.delete(0,"end")
    WebsiteEntry.delete(0,"end")
    HiddenLabel.configure(text="")   
    WidthEntry.focus() 

def open_new_window():
    main2= Toplevel()
    main2.title("About")
    main2.geometry("250x200")
    SpaceLabel =Label(main2, text= "  ")
    SpaceLabel.grid(column=0,row=0)
    LabelAbout = Label(main2, text ="Auto/Manual Web Clicker",font =("Helvetica",14))
    LabelAbout.grid(column=1,row=0,columnspan=3)
    LabelAuthor = Label(main2, text = "Author: Roman Chruszcz", font =("Helvetica",10), pady = 9, fg = "blue")
    LabelAuthor.grid(column=0, row =1, columnspan =3)

main = Tk()
main.title("Auto/Manual Web Clicker")
main.geometry("520x550")
my_menu = Menu(main,bg="white")
main.config(menu=my_menu)

file_menu = Menu(my_menu,bg="white")
help_menu = Menu(my_menu,bg="white")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Reset", command=reset_command)
file_menu.add_command(label="Quit", command=main.quit)
my_menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About", command=open_new_window)



Pic1= PhotoImage(file="images/mouse1.png")
Pic2= PhotoImage(file="images/mouse2.png")
Pic3= PhotoImage(file="images/mouse3.png")
Pic4= PhotoImage(file="images/mouse4.png")

TitleLabel = Label(main, text= "Set parameters for Your clicking:",font=("Helvetica", 24),pady = 20,padx = 5)
TitleLabel.grid(column = 0, row = 0, columnspan = 8)
SpanLabel = Label(main, text = "    ")
SpanLabel.grid(column = 0,row = 1)

SettingLabel = Label(main, text = "Choose type of settings:", font= ("Helvetica", 12),pady = 20)
SettingLabel.grid(column = 0, row = 1, columnspan = 3)

MouseLabel = Label(main, text = "Choose mouse button:", font= ("Helvetica", 12),pady = 20)
MouseLabel.grid(column = 5, row = 1, columnspan = 5)

AutoButton = Button(main, text = "Auto",font= ("Helvetica", 12), bg="blue", fg = "white", width = 10, command=auto)
AutoButton.grid(column = 1,row =2)
ManualButton = Button(main, text = "Manual",font= ("Helvetica", 12), bg="blue", fg = "white", width = 10,command=manual)
ManualButton.grid(column = 2,row =2)




ButtonLeft = Button(main,image = Pic1, borderwidth =0,command=selected_left)
ButtonLeft.grid(column =5, row=2,sticky=E,rowspan =2)
ButtonMiddle = Button(main, image= Pic2, borderwidth = 0,command= selected_middle)
ButtonMiddle.grid(column=6, row=2,sticky= W,rowspan =2)
ButtonRight = Button (main, image= Pic3, borderwidth = 0,command=selected_right)
ButtonRight.grid(column= 7, row =2,sticky = W,rowspan =2)
ButtonNone = Label(main, image= Pic4, borderwidth = 0)
ButtonNone.grid(column=5, row=4, columnspan = 3,rowspan= 3)
HiddenLabel = Label(main,text = "     ", font = ("Helvetica", 8))
HiddenLabel.grid(column=5, row =7, columnspan = 3)

WidHeiLabel = Label(main, text = "Set coordinates in pixels:", font= ("Helvetica", 12),pady = 20)
WidHeiLabel.grid(column = 1, row = 3,columnspan = 4, rowspan =3, sticky = N)



WidthEntry = Entry(main, width= 15,state=DISABLED)
WidthEntry.grid(column = 1, row = 4)
HeightEntry = Entry (main, width = 15,state=DISABLED)

HeightEntry.grid(column = 2, row = 4)

OptionsLabel = Label(main, text="Set options:",font= ("Helvetica", 12))
OptionsLabel.grid(column = 1, row=5,columnspan =2)

NumClicksLabel = Label(main, text= "Number of clicks:", font= ("Helvetica",12))
NumClicksLabel.grid(column =1, row =6)

NumClicks = Entry(main, width= 15)
NumClicks.grid(column = 2, row = 6)

IntervalLabel = Label(main, text= "Clicks interval:", font=("Helvetica",12))
IntervalLabel.grid(column=1, row=7)

Interval = Entry(main, width = 15)
Interval.grid(column=2, row=7)

spacerLabel = Label(main, text= "  ")
spacerLabel.grid(column=1,row= 8,columnspan=2)

WebsiteLabel = Label(main, text= "Enter website address:",pady = 10, font =("Helvetica",12))
WebsiteLabel.grid(column=1,row= 9,columnspan=2)

WebsiteEntry = Entry(main, width = 35)
WebsiteEntry.grid(column=1, row =10, columnspan = 2)

spacerLabel1 = Label(main, text= "  ")
spacerLabel1.grid(column=1,row= 11,columnspan=2)

StartButton= Button(main, text = "START", font = ("Helvetica", 22), bg = "green", fg = "white")
StartButton.grid(column =5, row=10, columnspan =3)

main.mainloop()