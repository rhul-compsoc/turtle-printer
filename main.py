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

# Add a CodeView for code input
editor = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme="monokai", width=50)
editor.pack(fill=Y, side=LEFT)

# Add a text widget for help
Label(root, text="lorem ipsum").pack()

canvas = Canvas(root, width=900)

def run_code():
    run_turtle(editor.get("1.0", "end-1c"), canvas)

# Add a button menu for turtle code
button_menu = Frame(root)
button_menu.pack()
run_btn = Button(button_menu, text=">> Run Code >>", command=run_code).pack()

# Add canvas for displaying turtle graphics
canvas.pack(fill=Y, side=RIGHT)
canvas.configure(bg="cyan")

root.mainloop()