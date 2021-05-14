from tkinter import *
import time
import pyautogui


main = Tk()
main.title("Auto/Manual Clicker")
main.geometry("500x500")




def runauto():
   
    mylabel= Label(main, text ="Your mouse cursor position will be set for clicking in:")
    mylabel.grid(column=1, row =5)

    calc()

def calc():
    x = 5
    while x > 0:
    
        time.sleep(1)
        
        x = x-1
        b = str(x)

    myLabel2 = Label(main, text=b)
    myLabel2.grid(column=1,row=6)

    # pyautogui    tu wstawic cala funkcje klikania

    
#AutoClick = Button(text="Press to autoselect clicking point by mouse cursor",command= runauto)
#AutoClick.grid(column =1, row = 1)
#AutoClick2 = Button(text="click",command= main2)
#AutoClick.grid(column =1, row = 1)

#Manual = Label(text = "Input coordinates in pixels below to select clicking point")
#Manual.grid(column=1, row = 2)

Pic1= PhotoImage(file="images/mouse1.png")
Pic2= PhotoImage(file="images/mouse2.png")
Pic3= PhotoImage(file="images/mouse3.png")
Pic4= PhotoImage(file="images/mouse4.png")

Label1 = Label(main,text= "      ")
Label1.grid(column=0,row=0,columnspan = 8, rowspan=2)
#Label2 = Label(main,text= "Choose type of position set")
#Label2.grid(column= 3,row=0,columnspan = 3)


#ButtonAuto = Button(main,text= "Auto Click")
#ButtonAuto.grid(column =3, row=1)
#ButtonManual = Button(main,text= "Manual Click")
#ButtonManual.grid(column=4, row=1)

ButtonLeft = Button(main,image = Pic1, borderwidth =0)
ButtonLeft.grid(column =2, row=2)
ButtonMiddle = Button(main, image= Pic2, borderwidth = 0)
ButtonMiddle.grid(column=3, row=2)
ButtonRight = Button (main, image= Pic3, borderwidth = 0)
ButtonRight.grid(column= 4, row =2)
ButtonNone = Label(main, image= Pic4, borderwidth = 0)
ButtonNone.grid(column=2, row=3, columnspan = 3)

TextBoxWebSite=Entry(main,text= "Insert website address to be opened", width=25,bg="white",fg="black")
TextBoxWebSite.insert(0,"website address")
TextBoxWebSite.grid(column=1,row=3)


TextBoxWidth = Entry(main, text = "Width in pixels", width = 10, bg = "white", fg="black")
TextBoxWidth.insert(1,"Width")
TextBoxWidth.grid(column=1, row = 4)

TextBoxHeight = Entry(main,text = "Height in pixels", width = 10, bg= "white", fg = "black")
TextBoxHeight.insert(2,"Height")
TextBoxHeight.grid(column=1, row = 5)


main.mainloop()

