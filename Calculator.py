import tkinter as tk
from math import *

calculation = ""

# Color scheme
BG_COLOR = "#2d2d2d"
DISPLAY_COLOR = "#1c1c1c"
BUTTON_COLOR = "#404040"
OPERATOR_COLOR = "#ff9500"
SCIENCE_COLOR = "#a6a6a6"
TEXT_COLOR = "#ffffff"
SPECIAL_COLOR = "#d4d4d2"

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        # Replace mathematical constants and functions
        calculation = calculation.replace("π", str(pi))
        calculation = calculation.replace("e", str(e))
        calculation = calculation.replace("^", "**")
        
        # Handle trigonometric functions
        calculation = calculation.replace("sin", "math.sin")
        calculation = calculation.replace("cos", "math.cos")
        calculation = calculation.replace("tan", "math.tan")
        calculation = calculation.replace("log", "math.log10")
        calculation = calculation.replace("ln", "math.log")
        
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("400x600")
root.title("Scientific Calculator")
root.configure(bg=BG_COLOR)

# Display Frame
display_frame = tk.Frame(root, bg=DISPLAY_COLOR, bd=2, relief=tk.FLAT)
display_frame.pack(padx=10, pady=10, fill=tk.X)

text_result = tk.Text(display_frame, height=2, width=24, font=("Helvetica", 30), 
                     bg=DISPLAY_COLOR, fg=TEXT_COLOR, bd=0, wrap=tk.WORD)
text_result.pack(padx=10, pady=10)
text_result.insert(1.0, "0")

# Button Frame
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Button styles
button_style = {
    "font": ("Helvetica", 18),
    "bd": 0,
    "fg": TEXT_COLOR,
    "activeforeground": TEXT_COLOR
}

# Scientific buttons
sci_buttons = [
    ("sin", 1, 0, SCIENCE_COLOR), ("cos", 1, 1, SCIENCE_COLOR), 
    ("tan", 1, 2, SCIENCE_COLOR), ("^", 1, 3, OPERATOR_COLOR),
    ("π", 2, 0, SCIENCE_COLOR), ("e", 2, 1, SCIENCE_COLOR),
    ("log", 2, 2, SCIENCE_COLOR), ("ln", 2, 3, SCIENCE_COLOR),
    ("(", 3, 0, OPERATOR_COLOR), (")", 3, 1, OPERATOR_COLOR),
    ("√", 3, 2, SCIENCE_COLOR), ("!", 3, 3, SCIENCE_COLOR)
]

for (text, row, col, color) in sci_buttons:
    btn = tk.Button(button_frame, text=text, bg=color, 
                   command=lambda t=text: add_to_calculation(t), **button_style)
    btn.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)

# Number buttons
num_buttons = [
    ("7", 4, 0, BUTTON_COLOR), ("8", 4, 1, BUTTON_COLOR), 
    ("9", 4, 2, BUTTON_COLOR), ("/", 4, 3, OPERATOR_COLOR),
    ("4", 5, 0, BUTTON_COLOR), ("5", 5, 1, BUTTON_COLOR),
    ("6", 5, 2, BUTTON_COLOR), ("*", 5, 3, OPERATOR_COLOR),
    ("1", 6, 0, BUTTON_COLOR), ("2", 6, 1, BUTTON_COLOR),
    ("3", 6, 2, BUTTON_COLOR), ("-", 6, 3, OPERATOR_COLOR),
    ("0", 7, 0, BUTTON_COLOR), (".", 7, 1, BUTTON_COLOR),
    ("=", 7, 2, OPERATOR_COLOR), ("+", 7, 3, OPERATOR_COLOR)
]

for (text, row, col, color) in num_buttons:
    if text == "=":
        btn = tk.Button(button_frame, text=text, bg=color, 
                       command=evaluate_calculation, **button_style)
    else:
        btn = tk.Button(button_frame, text=text, bg=color, 
                       command=lambda t=text: add_to_calculation(t), **button_style)
    btn.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)

# Clear button
clear_btn = tk.Button(button_frame, text="C", bg=SPECIAL_COLOR, 
                     command=clear_field, **button_style)
clear_btn.grid(row=0, column=3, sticky=tk.NSEW, padx=2, pady=2)

# Configure grid weights
for i in range(8):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

root.mainloop()
