# Food on the Go
# SDEV220 Mr. Lonnie
# Fantahun, Dakota, Ella, Charles
# This project 

# Importing Working module
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

Root = Tk()

# Title
Root.title("Food On The Go")

#Icon in the corner image
Image = ImageTk.PhotoImage(file = "car.PNG")
Root.iconphoto(False, Image)

# Background color
Root.configure(bg = "azure")

# Define my NameLabel before my function so I can delete it if the user tries different names
NameLabel = Label(Root)

# A function to display the user's name
def HelloName():
    global NameLabel

    if InputName.get() == "":
        messagebox.showerror(title = "Name Error", message = "Please enter your name.")

    elif InputEmail.get() == "":
        messagebox.showerror(title = "Name Error", message = "Please enter your Email.")

    else:
        # This deletes any name that the label is holding 
        NameLabel.destroy()
        
        
        # Size
        Root.geometry("860x630")
        
        # This label greets the user by their name
        NameLabel = Label(Root, text = "Hello " + InputName.get(), font=("Comic Sans MS", 20), justify = "center")
        NameLabel.configure(bg = "azure")
        NameLabel.grid(row = 8, column = 1, sticky = "W")
    

        # Order button
        StartOrderButton = Button(Root, text = "Start Ordering!", font=("Comic Sans MS", 15), command = NewWindow)
        StartOrderButton.configure(bg = "white", fg = "black")
        StartOrderButton.grid(row = 9, column = 2, sticky = "W")

# Size
Root.geometry("780x535")

# Ctreating labels (or print statements)
MainLabel = Label(Root, text = "Hello and Welcome to Food on the Go!", padx = 50, font=("Comic Sans MS", 24), justify = "center")
MainLabel.configure(bg = "white")
MainLabel.grid(row = 0, column = 0, columnspan = 4)

# A space between rows
MySpaceLabel = Label(Root)
MySpaceLabel.configure(bg = "azure")
MySpaceLabel.grid(row = 1, column = 0)

# Car picture
Car = PhotoImage(file = "car.PNG")
CarPic = Label(Root, text = "Car", image = Car)
CarPic.grid(row = 10, column = 3)

#CarPic = Label(Root, text = "Car", image = Car)
#CarPic.grid(row = 10, column = 3)

# Enter Username Label
EnterNameLabel = Label(Root, text = "Username", font=("Comic Sans MS", 20), justify = "center")
EnterNameLabel.configure(bg = "azure")
EnterNameLabel.grid(row = 2, column = 1, sticky = "W")

# Input Username
InputName = Entry(Root, text = "Please enter your name.", font=("Comic Sans MS", 22), justify = "left")
InputName.grid(row = 3, column = 1, sticky = "W")

# Enter Email Label
EnterEmailLabel = Label(Root, text = "Email", font=("Comic Sans MS", 20), justify = "center")
EnterEmailLabel.configure(bg = "azure")
EnterEmailLabel.grid(row = 4, column = 1, sticky = "W")

#if EnterEmailLabel 

# Input Email
InputEmail = Entry(Root, text = "Please enter your Email.", font=("Comic Sans MS", 22), justify = "left")
InputEmail.grid(row = 5, column = 1, sticky = "W")

# Submit name button
NameButton = Button(Root, text = "Submit", command = HelloName, font=("Comic Sans MS", 15))
NameButton.configure(bg = "white", fg = "black")
NameButton.grid(row = 6, column = 2, sticky = "W")

# A space between rows
MySpaceLabel = Label(Root)
MySpaceLabel.configure(bg = "azure")
MySpaceLabel.grid(row = 7, column = 1)


# SECOND WINDOW HURRAY!!!
def NewWindow():

    # New window and name
    GameWindow = Toplevel()
    GameWindow.title("Donuts Page")
    GameWindow.configure(bg = "azure")

    
    #Icon in the corner image
    Image = ImageTk.PhotoImage(file = "car.PNG")
    GameWindow.iconphoto(False, Image)

    # Size of the window
    GameWindow.geometry("1000x700")


    # Class 1
    # 2 basic types of donuts are yeast and cake
    class Yeast():
      def __init__(self, yeast):
        self.yeast = yeast
    

    # Class 2
    class Cake():
        def __init__(self, cake):
            self.cake = cake


    # A function to display the user's name
    '''def SendYeast():

        if InputYeast.get() == "":
            messagebox.showerror(title = "Name Error", message = "Please enter a number from 0-12.")

        elif InputYeast.get() <0 and InputYeast.get() > 12:
            messagebox.showerror(title = "Name Error", message = "Please enter a number from 0-12 test.")

        else:
        InputYeast.get(GameWindow, command = Yeast)'''

            
    # This class contains the different toppings
    '''class Toppings(Donuts):
        def __init__(self, chocolate, caramel, maple):
            self.chocolate = chocolate
            self.caramel = caramel
            self.maple = maple'''



    # Donut picture
    Pic = PhotoImage(file = "donut.PNG")
    DonutPic = Label(GameWindow, text = "donut", image = Pic)
    DonutPic.grid(row = 0, column = 0, columnspan = 4)
    
    # Ctreating labels (or print statements)
    DonutPageLabel = Label(GameWindow, text = "What You Would Like?\nYeast or Cake Donut?", font=("Comic Sans MS", 24), justify = "center")
    DonutPageLabel.configure(bg = "azure")
    DonutPageLabel.grid(row = 1, column = 1)

    # Space label
    SpaceLabel = Label(GameWindow, text = "", padx = 20, font=("Comic Sans MS", 24), justify = "center")
    SpaceLabel.configure(bg = "azure")
    SpaceLabel.grid(row = 2, column = 1, sticky = "W")

    # Space label
    SpaceLabel2 = Label(GameWindow, text = "", padx = 20, font=("Comic Sans MS", 24), justify = "center")
    SpaceLabel2.configure(bg = "azure")
    SpaceLabel2.grid(row = 3, column = 1, sticky = "W")

    # Yeast label
    YeastLabel = Label(GameWindow, text = "How many yeast donuts?", font=("Comic Sans MS", 18), justify = "left")
    YeastLabel.configure(bg = "azure")
    YeastLabel.grid(row = 4, column = 0, sticky = "W")

    # Input donut type 
    InputYeast = Entry(GameWindow, text = "",font = ("Comic Sans MS", 22), justify = "left")
    InputYeast.grid(row = 5, column = 0, sticky = "W")

    # Submit donut type button
    yeastButton = Button(GameWindow, text = "Submit", command = Yeast, font=("Comic Sans MS", 15))
    yeastButton.configure(bg = "white", fg = "black")
    yeastButton.grid(row = 5, column = 1, sticky = "W")


    # Space label
    SpaceLabel3 = Label(GameWindow, text = "", padx = 20, font=("Comic Sans MS", 24), justify = "center")
    SpaceLabel3.configure(bg = "azure")
    SpaceLabel3.grid(row = 6, column = 1, sticky = "W")

    # Cake label
    CakeLabel = Label(GameWindow, text = "How many cake donuts?", font=("Comic Sans MS", 18), justify = "left")
    CakeLabel.configure(bg = "azure")
    CakeLabel.grid(row = 7, column = 0, sticky = "W")

    # Input donut type 
    InputCake = Entry(GameWindow, text = "",font = ("Comic Sans MS", 22), justify = "left")
    InputCake.grid(row = 8, column = 0, sticky = "W")

    # Submit donut type button
    CakeButton = Button(GameWindow, text = "Submit", command = Cake, font=("Comic Sans MS", 15))
    CakeButton.configure(bg = "white", fg = "black")
    CakeButton.grid(row = 8, column = 1, sticky = "W")

    donutsDict = {100: Glazed,
              200: Long John,
              300: Creme Filled,
              400: Holland,
              500: Cake Donuts,
              600: Powdered Donuts,
              700: Jelly Donuts,
              900: Sour Creme,
              1000: Crullers,
              
             }

   
