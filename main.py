from tkinter import *
from tkinter.ttk import *
from chlorophyll import CodeView
import pygments.lexers

# Create root window
root = Tk()
root.title("Turtle Printer")
# Make tkinter window the size of the screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Add a CodeView for code input
editor = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme="monokai").pack(fill=Y, side=LEFT)

# Add a text widget for help
help_text = Label(root, text="lorem ipsum").pack()

# Add a button menu for turtle code
button_menu = Frame(root).pack(side=RIGHT)
run_btn = Button(button_menu, text=">> Run Code >>").pack()

# Add canvas for displaying turtle graphics


root.mainloop()