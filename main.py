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

# Make a frame to display user errors in
error_frame = Frame(root)
error_frame.grid(column=1, row=2, sticky="s")
error_frame.columnconfigure((0, 1), weight=1)
error_frame.rowconfigure((0, 1), weight=1)

error_label = Text(error_frame, wrap=NONE, height=15)
error_label.grid(column=0, row=0)

h = Scrollbar(error_frame, orient="horizontal", command=error_label.xview)
h.grid(column=0, row=1, sticky="ew")
error_label.config(xscrollcommand=h.set)

v = Scrollbar(error_frame, orient="vertical", command=error_label.yview)
v.grid(column=1, row=0, sticky="ns")
error_label.config(yscrollcommand=v.set)

error_label.config(state=DISABLED)
error_label.config(fg="red")

# Make a canvas to display the turtle on
canvas = Canvas(root, width=750)
canvas.grid(column=2, row=0, rowspan=3, sticky="news")

# display_error writes and error to the error text field
def display_error(error):
        # Write error to text field
        error_label.config(state=NORMAL)
        error_label.delete("1.0", END)
        error_label.insert("end", error)
        error_label.config(state=DISABLED)

# This will be run when the "Run Code" button is pressed
def run_code():
    try:
        run_turtle(editor.get("1.0", "end-1c"), canvas)
    except SyntaxError as e:
        # Create and display a more readable syntax error
        error = f"Your code contains a syntax error:\nError on line {e.lineno} col {e.offset}:\n{e.text}\n{' ' * (e.offset - 1)}^\n{e.msg}"
        display_error(error)
    except Exception as e:
        pass

# Add a button menu for turtle code
button_menu = Frame(root)
button_menu.grid(column=1, row=1)
run_btn = Button(button_menu, text=">> Run Code >>", command=run_code).grid(column=0, row=0)

root.mainloop()