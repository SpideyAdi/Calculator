import tkinter as tk #pulls from tkinter library

root = tk.Tk() #starts code using tkinter
root.title("Calculator") # adds title to window
root.geometry("400x600") #size of window
root.configure(bg="black") #adds background color

expression = "" #creates empty string

# DISPLAY
display = tk.Entry( #starts display using tk
    root,
    font=("Arial", 32),#changes font and size
    bg="black", #background color
    fg="white", #foreground color
    justify="right", #starts text from right
    bd=0, #no border
    highlightthickness=0, #no highlight thickness
    insertbackground="white" #color of blinking text cursor
)
display.pack(fill="both", ipadx=10, ipady=25)#adds padding 

# FUNCTIONS
def press(value): #captures value, concatinates to current numbers, enters value, adds to current elements
    global expression #changes expression to a global variable
    print("inside press function, value:",value) 
    if value == "x": #creates an if statement making value of x == *
        expression += "*" #expression = expression + "*"
    else: #else block gets executed when any other value than x is pressed
        expression += value #expression += value

    display.delete(0, tk.END) #clears contents of display
    display.insert(0, expression.replace("*", "x")) #insert updates current expression in display
    print ("This is expression ", expression)

def clear(): #creates clear function: gets called when press on c button
    global expression #expression is now global
    expression = "" # reinstating value of expression
    display.delete(0, tk.END) #clearing display

def equal(): #creates equal function that gets called on when equal button is pressed
    global expression #changes expression to global
    try: #makes it so that no matter what, the equal button must try to evaluate expressions
        result = str(eval(expression)) #makes result variable that evaluates the expression and turns it into string
        display.delete(0, tk.END) #clears current values in display
        display.insert(0, result) #enters the result of the equation in the display
        expression = result #makes it sio that the expression variable is equal to the result variable
    except: #if the code cannot be evaluted however..,
        display.delete(0, tk.END) #clears display
        display.insert(0, "Error") #enters the string, "Error" onto the display
        expression = "" #makes expression a blank string
        
# FRAME
frame = tk.Frame(root, bg="black") #creates a frame and changes its background color to black
frame.pack(expand=True, fill="both") #lets the values inside the frame expand as the frame expands and lets the frame stretch in both directions

buttons = [ #begins a list under the variable buttons
    "C", "+/-", "%", "/",# creates top line of buttons
    "7", "8", "9", "x",#creates second line of buttons
    "4", "5", "6", "-", #creates third line of buttons
    "1", "2", "3", "+", #creates fourth line of buttons
    "0", ".", "=" #creates last line of buttons
]# ends the list

row = 0 #starts button placement at row 0
col = 0#starts button placement at column 0

for btn in buttons: #loops through every button in the buttons list

    def cmd(x=btn): #creates a command for the following button
        if x == "C": #there is a command made for the C button
            clear() #the clear button activates when C is pressed
        elif x == "=": #but if the equal button is pressed
            equal() #then the equal button activates
        else: #and if any other button is pressed
            press(x) #that button goes to the press function

    # COLORS
    if btn in ["+", "-", "/", "x", "="]: #checks if the button is an operator
        bg_color = "#ff9f0a" #sets operator background color to orange
        fg_color = "black"  #sets operator text color to black
    elif btn in ["C", "+/-", "%"]:#checks if the button is a function button
        bg_color = "#a5a5a5" #sets function button background color to gray
        fg_color = "black" #sets function button text color to black
    else: #all remaining buttons are number buttons
        bg_color = "#333333"  #sets number button background color to dark gray
        fg_color = "black" #sets number button text color to black

    tk.Button( 
        frame,#places the button inside the frame
        text=btn,#sets the text displayed on the button
        font=("Arial", 20), #sets the font style and font size

        fg=fg_color, #sets the text color
        bg=bg_color, #sets the background color

        activebackground=bg_color,  #keeps the same background color when the button is pressed
        activeforeground=fg_color,  #keeps the same text color when the button is pressed
    
        bd=0,  #removes the button border
        relief="flat",  #gives the button a flat appearance
        highlightthickness=0,  #removes the highlight border
        takefocus=0,  #prevents the button from receiving keyboard focus
    
        command=cmd  #calls the cmd() function when the button is clicked
    ).grid(
        row=row,  #places the button in the current row
        column=col,  #places the button in the current column
        sticky="nsew",  #stretches the button to fill the entire grid cell
        padx=3,  #adds horizontal spacing around the button
        pady=3  #adds vertical spacing around the button
    )
    
    col += 1  #moves to the next column

    if col > 3:  #checks if four columns have been filled
        col = 0  #resets the column back to the first column
        row += 1  #moves down to the next row
    
    # GRID RESIZE
    for i in range(5):  #loops through all five rows
        frame.grid_rowconfigure(i, weight=1)  #allows each row to expand equally when the window is resized
    
    for j in range(4):  #loops through all four columns
        frame.grid_columnconfigure(j, weight=1)  #allows each column to expand equally when the window is resized

root.mainloop()  #starts the Tkinter event loop and keeps the window running until the window is closed
