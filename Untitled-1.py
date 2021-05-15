from tkinter import *
import time
import pyautogui


main = Tk()
main.title("Auto/Manual Clicker")
main.geometry("550x550")

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

AutoButton = Button(main, text = "Auto",font= ("Helvetica", 12), bg="blue", fg = "white", width = 10)
AutoButton.grid(column = 1,row =2)
ManualButton = Button(main, text = "Manual",font= ("Helvetica", 12), bg="blue", fg = "white", width = 10)
ManualButton.grid(column = 2,row =2)




ButtonLeft = Button(main,image = Pic1, borderwidth =0)
ButtonLeft.grid(column =5, row=2,sticky=E,rowspan =2)
ButtonMiddle = Button(main, image= Pic2, borderwidth = 0)
ButtonMiddle.grid(column=6, row=2,sticky= W,rowspan =2)
ButtonRight = Button (main, image= Pic3, borderwidth = 0)
ButtonRight.grid(column= 7, row =2,sticky = W,rowspan =2)
ButtonNone = Label(main, image= Pic4, borderwidth = 0)
ButtonNone.grid(column=5, row=4, columnspan = 3,rowspan= 3)

WidHeiLabel = Label(main, text = "Set coordinates in pixels:", font= ("Helvetica", 12),pady = 20)
WidHeiLabel.grid(column = 1, row = 3,columnspan = 4, rowspan =3, sticky = N)



WidthEntry = Entry(main, width= 15)
WidthEntry.insert(0,"width")
WidthEntry.grid(column = 1, row = 4)
HeightEntry = Entry (main, width = 15)
HeightEntry.insert(1,"height")
HeightEntry.grid(column = 2, row = 4)

OptionsLabel = Label(main, text="Set options:",font= ("Helvetica", 12))
OptionsLabel.grid(column = 1, row=5)
NumClicksLabel = Label(main, text= "Number of clicks:", font= ("Helvetica",12))
NumClicksLabel.grid(column =1, row =6)
NumClicks = Entry(main, width= 15)
NumClicks.grid(column = 2, row = 6)
IntervalLabel = Label(main, text= "Clicks interval:", font=("Helvetica",12))
IntervalLabel.grid(column=1, row=7)
Interval = Entry(main, width = 15)
Interval.grid(column=2, row=7)

WebsiteLabel = Label(main, text= "Enter website address:", font =("Helvetica",12))
WebsiteLabel.grid(column=2,row= 8)

main.mainloop()