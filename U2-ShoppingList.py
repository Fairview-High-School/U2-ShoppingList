# For more information about turtle, see 
#     the Resources folder for the course.
#     https://docs.python.org/3/library/turtle.html
#     https://blog.trinket.io/using-images-in-turtle-programs/
# List commands of note:
#     mylist.append(x) -- Add item x to the end of the list.
#     mylist.insert(pos, x)  -- Add item x to the list, after position pos.  Note the first position in python is 0
#     mylist.remove(x) -- Remove item x from the list.
#     mylist.clear()   -- Clears the list
# Print and input commands
#     print("text") or print(variable)
#     answer = input("Enter an answer to this prompt: ") -- 
# messagebox and simpledialog prompts
#     messagebox.showinfo("Title", "Message") -- Displays a message box with an OK button
#     response = messagebox.showyesno("Title", "Message") -- Displays a message box with Yes and No buttons, returns True if Yes is clicked, False if No is clicked
#     answer = simpledialog.askstring("Title", "Prompt") -- Displays a prompt for the user to enter a string


###################################################
import turtle
from tkinter import messagebox, simpledialog

shoppingList = []

def addItem(x,y): 
    return

def deleteItem(x,y):
    return
   
def clearList(x,y):
    return

def displayList(x,y):
    return
    

#########################################################
#main script
screen = turtle.Screen()
addItemCostume = "AddItem.gif"
deleteItemCostume = "DeleteItem.gif"
clearListCostume = "ClearList.gif"
showListCostume = "ShowList.gif"

screen.addshape(addItemCostume)
screen.addshape(deleteItemCostume)
screen.addshape(clearListCostume)
screen.addshape(showListCostume)

#Create Turtle Buttons
addItemButton = turtle.Turtle()
addItemButton.penup()
addItemButton.shape("AddItem.gif")
deleteItemButton = turtle.Turtle()
deleteItemButton.penup()
deleteItemButton.shape("DeleteItem.gif")
clearListButton = turtle.Turtle()
clearListButton.penup()
clearListButton.shape("ClearList.gif")
showListButton = turtle.Turtle()
showListButton.penup()
showListButton.shape("ShowList.gif")

#Position Turtle Buttons
addItemButton.goto(0,75)
addItemButton.left(90)
deleteItemButton.goto(0,25)
deleteItemButton.left(90)
clearListButton.goto(0,-25)
clearListButton.left(90)
showListButton.goto(0,-75)
showListButton.left(90)

#add Turtle Specific Scripts
addItemButton.onclick(addItem)  #runs the function addItem, sending it the x and y coordinate of the click, when addItemButton is clicked.
deleteItemButton.onclick(deleteItem)
clearListButton.onclick(clearList)
showListButton.onclick(displayList)

turtle.mainloop()

