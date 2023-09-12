from tkinter import *
from tkinter.ttk import *
from chlorophyll import CodeView
import pygments.lexers

# Create root window
root = Tk()
root.title("Turtle Printer")

# Add a CodeView for code input
editor = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme="monokai").grid()

root.mainloop()