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
root.rowconfigure(tuple(range(2)), weight=1)

# Add a CodeView for code input
editor = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme="monokai", width=50)
editor.grid(column=0, row=0, rowspan=2, sticky="news")

# Add a text widget for help
Label(root, text="lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet", justify=LEFT, wraplength=500).grid(column=1, row=0)

canvas = Canvas(root, width=800)

# This will be run when the "Run Code" button is pressed
def run_code():
    run_turtle(editor.get("1.0", "end-1c"), canvas)

# Add a button menu for turtle code
button_menu = Frame(root)
button_menu.grid(column=1, row=1)
run_btn = Button(button_menu, text=">> Run Code >>", command=run_code).grid(column=0, row=0)

# Add canvas for displaying turtle graphics
canvas.grid(column=2, row=0, rowspan=2, sticky="news")
canvas.configure(bg="cyan")

root.mainloop()