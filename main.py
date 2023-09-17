from tkinter import *
from tkinter.ttk import *
from chlorophyll import CodeView
from PIL import Image, ImageChops
from dotenv import load_dotenv
import pygments.lexers
import traceback
import io
import socket
import os
import sys
from interpreter import run_turtle
from help import *

load_dotenv()

try:
    SERVER_ADDRESS = (os.environ["TURTLE_ADDRESS"], int(os.environ["TURTLE_PORT"]))
except KeyError as e:
    print(f"Missing config value {e}")
    sys.exit(1)
except ValueError:
    print('Config value TURTLE_PORT must be an integer')
    sys.exit(1)

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
help_frame = Frame(root)
help_frame.grid(column=1, row=0)
help_frame.columnconfigure(0, weight=1)
help_frame.rowconfigure((0, 1), weight=1)

help_page = 0
help_var = StringVar(value=help[help_page])
help_label = Label(help_frame, textvariable=help_var, justify=LEFT, wraplength=550)
help_label.grid(column=0, row=0, sticky="n")

help_buttons = Frame(help_frame)
help_buttons.grid(column=0, row=1, sticky="news", pady=20)

page_number_var = StringVar()
page_number = Label(help_buttons, textvariable=page_number_var)
page_number.grid(column=1, row=0, padx=70)

# update_page_number updates the page number display
def update_page_number():
    global help_page
    page_number_var.set(f"{help_page + 1}/{len(help)}")
    
    # Update the button states
    if help_page == len(help) - 1:
        next_button.config(state=DISABLED)
    else:
        next_button.config(state=NORMAL)
    
    if help_page == 0:
        prev_button.config(state=DISABLED)
    else:
        prev_button.config(state=NORMAL)

# next_page moves the help window a page forward
def next_page():
    global help_page
    if help_page < len(help) - 1:
        help_page += 1
        help_var.set(help[help_page])
        update_page_number()

# prev_page moves the help window back a page
def prev_page():
    global help_page
    if help_page > 0:
        help_page -= 1
        help_var.set(help[help_page])
        update_page_number()


next_button = Button(help_buttons, text="Next", command=next_page)  
next_button.grid(column=2, row=0)

prev_button = Button(help_buttons, text="Prev", command=prev_page)
prev_button.grid(column=0, row=0)
update_page_number()

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
error_label.tag_config("error", foreground="red")

# Make a canvas to display the turtle on
canvas = Canvas(root, width=750)
canvas.grid(column=2, row=0, rowspan=3, sticky="news")

# display_text writes text to the error text field
def display_text(text):
    error_label.config(state=NORMAL)
    error_label.insert("end", text)
    error_label.config(state=DISABLED)

# print_text prints text to the error field
def print_text(text):
    display_text(str(text) + "\n")

# display_error writes and error to the error text field
def display_error(error):
        # Write error to text field and add color tag
        start = error_label.index("end-1c")
        display_text(error)
        end = error_label.index("end-1c")
        error_label.tag_add("error", start, end)

# clear_error will clear the current error from the text field
def clear_error():
    error_label.config(state=NORMAL)
    error_label.delete("1.0", END)
    error_label.config(state=DISABLED)

# This will be run when the "Run Code" button is pressed
def run_code():
    clear_error()
    try:
        # Disable buttons during execution
        run_button.config(state=DISABLED)
        save_button.config(state=DISABLED)

        run_turtle(editor.get("1.0", "end-1c"), canvas, print_text)
    except SyntaxError as e:
        # Create and display a more readable syntax error
        error = f"Your code contains a syntax error:\nError on line {e.lineno} col {e.offset}:\n{e.text}\n{' ' * (e.offset - 1)}^\n{e.msg}"
        display_error(error)
    except Exception as e:
        # Create and display the runtime error
        error = f"Your code caused an error during execution:\n{''.join(traceback.format_exception(e)[-2:])}"
        display_error(error)
    finally:
        # Re-enable buttons
        run_button.config(state=NORMAL)
        save_button.config(state=NORMAL)

# Add a button menu for turtle code
button_menu = Frame(root)
button_menu.grid(column=1, row=1, sticky="s")
run_button = Button(button_menu, text=">> Run Code >>", command=run_code)
run_button.grid(column=0, row=0, sticky="s")

# trim removes excess space from a PIL image
# by fraxel (StackOverflow)
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

# save_image will export the current canvas as a png and send it to be printed
def save_image():
    # Disable button
    save_button.config(state=DISABLED)
    # Export canvas to postscript
    ps = canvas.postscript()
    # Convert postscript to png
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    # Trim excess space
    img = trim(img)
    # Send image to the server
    send_image(img)

# send_image sends the given image to the image server
def send_image(img):
    # Convert image to byte array
    with io.BytesIO() as img_bytes:
        img.save(img_bytes, format="PNG")
        img_byte_array = img_bytes.getvalue()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to image server and send image length
                sock.connect(SERVER_ADDRESS)
                sock.sendall(len(img_byte_array).to_bytes(4, "big"))
                # Now send whole image
                sock.sendall(img_byte_array)
        except socket.error as error:
            display_error(f"Error connecting to {SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}\n{error}")

save_button = Button(button_menu, text="Print Image", command=save_image)
save_button.grid(column=0, row=1, pady=40)
save_button.config(state=DISABLED)

root.mainloop()