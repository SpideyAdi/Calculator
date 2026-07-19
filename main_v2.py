import tkinter as tk #pulls from tkinter library
import math

root = tk.Tk() #starts code using tkinter
root.title("Calculator") #adds title to window
root.geometry("400x600") #size of window
root.configure(bg="black") #adds background color

expression = "" #creates empty string
just_calculated = False #checks if equals was pressed
clear_timer = None #stores timer for long press

# DISPLAY
display = tk.Entry(
    root,
    font=("Arial", 32), #changes font and size
    bg="black", #background color
    fg="white", #foreground color
    justify="right", #starts text from right
    bd=0, #no border
    highlightthickness=0, #no highlight thickness
    insertbackground="white" #color of blinking text cursor
)

display.pack(fill="both", ipadx=10, ipady=25) #adds padding

# History label
history_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="black",
    fg="gray",
    anchor="e"
)
history_label.pack(fill="x", padx=10, pady=(0, 5))

# FUNCTIONS

def add_to_expression(value): #renamed from press() to make function clearer
    global expression, just_calculated #allows changing global variables

    print("inside add_to_expression function, value:", value)

    if just_calculated and value.isdigit(): #checks if result exists and number is pressed
        expression = "" #removes old result

    just_calculated = False #resets result tracker

    if value == ".": #checks if decimal button is pressed
        current_number = expression.split("+")[-1] #gets number after +
        current_number = current_number.split("-")[-1] #gets number after -
        current_number = current_number.split("*")[-1] #gets number after *
        current_number = current_number.split("/")[-1] #gets number after /

        if "." in current_number: #checks if decimal already exists
            return #stops another decimal from being added

    if value == "x": #checks if multiplication button is pressed
        expression += "*" #changes x into * for Python calculations

    else: #runs for all other buttons
        expression += value #adds value to expression

    display.delete(0, tk.END) #clears display

    display.insert(0, expression.replace("*", "x")) #updates display

    print("This is expression ", expression)


def clear(): #creates clear function
    global expression #allows changing expression

    expression = "" #resets expression

    display.delete(0, tk.END) #clears display

def equal():
    global expression, just_calculated

    if not expression:
        display.delete(0, tk.END)
        display.insert(0, "0")
        expression = "0"
        just_calculated = True
        return

    try:
        old_expression = expression

        result = str(eval(expression))

        display.delete(0, tk.END)
        display.insert(0, result)

        history_label.config(
            text=f"{old_expression.replace('*', 'x')} = {result}"
        )

        expression = result
        just_calculated = True

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

        history_label.config(text="")

        expression = ""
        just_calculated = False

def backspace(): #removes last entered character
    global expression #allows changing expression

    expression = expression[:-1] #removes last character

    display.delete(0, tk.END) #clears display

    display.insert(0, expression.replace("*", "x")) #updates display


def start_clear(event): #starts when C is held
    global clear_timer
    clear_timer = root.after(1000, clear)
    return "break" # Prevents other click events from firing

def stop_clear(event): #starts when C is released
    global clear_timer
    if clear_timer:
        root.after_cancel(clear_timer)
        clear_timer = None
        backspace() # Performs the backspace
    return "break" # Prevents other click events from firing


def handle_keypress(event): #creates keyboard listener function
    k = event.char #gets character typed
    n = event.keysym #gets system key name

    if k in "0123456789+-/.": #checks if basic math button is pressed
        add_to_expression(k) #adds symbol to expression
    elif k == "*": #checks if star key is pressed
        add_to_expression("x") #adds x to expression for multiplication
    elif k == "=" or n == "Return": #checks if equals or enter key is pressed
        equal() #runs equal function
    elif n == "BackSpace": #checks if delete key is pressed
        backspace() #runs backspace function
    elif n == "Escape": #checks if escape key is pressed
        clear() #runs clear function


# FRAME
frame = tk.Frame(root, bg="black") #creates frame

frame.pack(expand=True, fill="both") #lets frame expand


buttons = [
    "C", "+/-", "%", "x²",
     "7", "8", "9","√",
    "4", "5", "6", "π",
    "1", "2", "3", "/",
    "0", ".", " ", "x",
    " ","+","=","-"
]


row = 0 #starts button placement at row 0

col = 0 #starts button placement at column 0


for btn in buttons: #loops through every button


    def cmd(x=btn): #saves button value separately
        global expression #allows changing expression

        if x == "C" or x == " ": #checks if C or blank space is pressed
            pass #C uses press and release events

        elif x == "=": #checks if equal is pressed
            equal() #runs equal function


        elif x == "x²": #checks if square button is pressed

            if expression:
                expression = str(float(expression) ** 2)

                display.delete(0, tk.END)

                display.insert(0, expression)
                
        elif x == "π": #checks if pi button is pressed

            expression = str(math.pi)

            display.delete(0, tk.END)

            display.insert(0, expression) #FIXED: removed trailing .replace script crash

        elif x == "√": #checks if square root button is pressed

            if expression:
                expression = str(math.sqrt(float(expression)))

                display.delete(0, tk.END)

                display.insert(0, expression)
                

        elif x == "%": #checks if percent is pressed

            if expression: #checks if expression exists
                expression = str(float(expression) / 100) #converts to percent

                display.delete(0, tk.END) #clears display

                display.insert(0, expression) #shows result

        elif x == "+/-": #checks if negative button is pressed
        
            if expression.startswith("-"): #checks if number is negative
                expression = expression[1:] #removes negative

            else:
                expression = "-" + expression #adds negative

            display.delete(0, tk.END) #clears display

            display.insert(0, expression) #updates display

        else: #runs for other buttons
            add_to_expression(x) #calls renamed function
            


    # COLORS

    if btn in ["+", "-", "/", "x", "="]: #checks if button is an operator

        bg_color = "#ff9f0a" #sets operator background color to orange

        fg_color = "black" #sets operator text color to black

    elif btn in ["C", "+/-", "%", "x²", "√", "π"]: #checks if button is a function button

        bg_color = "#a5a5a5" #sets function button background color to gray

        fg_color = "black" #sets function button text color to black

    else: #all remaining buttons are number buttons

        bg_color = "#333333" #sets number button background color to dark gray

        fg_color = "white" #FIXED: set to white text so black numbers aren't hidden on dark gray background


    button = tk.Label(
        frame,
        text=btn,
        font=("Arial", 20),

        fg=fg_color,
        bg=bg_color,

        
    )
    button.bind("<Button-1>", lambda event, command_func=cmd: command_func())

    button.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=3,
        pady=3
    )


    if btn == "C": #checks if button is C

        button.bind(
            "<ButtonPress-1>",
            start_clear
        ) #starts long press timer

        button.bind(
            "<ButtonRelease-1>",
            stop_clear
        ) #short press removes character


    col += 1 #moves to next column


    if col > 3: #checks if four columns are filled

        col = 0 #resets column

        row += 1 #moves to next row

# GRID RESIZE
for i in range(6): #loops through five rows

    frame.grid_rowconfigure(i, weight=1) #allows rows to expand equally


for j in range(4): #loops through four columns

    frame.grid_columnconfigure(j, weight=1) #allows columns to expand equally

root.bind("<Key>", handle_keypress) #connects physical keyboard to listener function

root.mainloop() #starts Tkinter event loop
