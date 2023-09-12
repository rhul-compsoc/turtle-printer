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
editor = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme="monokai").grid()

root.mainloop()