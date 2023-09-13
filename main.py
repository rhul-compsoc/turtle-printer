from tkinter import *
from tkinter.ttk import *
from chlorophyll import CodeView
import pygments.lexers
from interpreter import run_turtle

# Create root window
root = Tk()
root.title("Turtle Printer")
# Make tkinter window the size of the screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.columnconfigure(tuple(range(3)), weight=1)
root.rowconfigure(tuple(range(3)), weight=1)

# Add a CodeView for code input
editor = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme="monokai", width=50)
editor.grid(column=0, row=0, rowspan=3, sticky="news")

# Add a text widget for help
Label(root, text="lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet", justify=LEFT, wraplength=500).grid(column=1, row=0)

canvas = Canvas(root, width=750)

# This will be run when the "Run Code" button is pressed
def run_code():
    run_turtle(editor.get("1.0", "end-1c"), canvas)

# Add a button menu for turtle code
button_menu = Frame(root)
button_menu.grid(column=1, row=1)
run_btn = Button(button_menu, text=">> Run Code >>", command=run_code).grid(column=0, row=0)

# Make a frame to display user errors in
error_frame = Frame(root)
error_frame.grid(column=1, row=2, sticky="s")
error_frame.columnconfigure((0, 1), weight=1)
error_frame.rowconfigure((0, 1), weight=1)

error_label = Text(error_frame, wrap=NONE)
error_label.grid(column=0, row=0)

h = Scrollbar(error_frame, orient="horizontal", command=error_label.xview)
h.grid(column=0, row=1, sticky="ew")
error_label.configure(xscrollcommand=h.set)

v = Scrollbar(error_frame, orient="vertical", command=error_label.yview)
v.grid(column=1, row=0, sticky="ns")
error_label.configure(yscrollcommand=v.set)

error_label.insert(END, "lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet")
error_label.config(state=DISABLED)

# Add canvas for displaying turtle graphics
canvas.grid(column=2, row=0, rowspan=3, sticky="news")

root.mainloop()