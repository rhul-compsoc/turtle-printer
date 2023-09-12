# Exclude all default globals from the sandbox
disallowed = globals().copy()

# Import allowed modules
import math
from turtle import *

# Remove disallowed globals and 'disallowed' object created earlier
allowed_globals = {k: v for k, v in globals().items() if k not in disallowed and k != "disallowed"}

# run_turtle runs the given code and exports the resulting turtle image to the given file
def run_turtle(code, file):
    # Compile the turtle code
    try:
        compiled = compile(code, "turtle", "exec")
    except SyntaxError:
        print("User code syntax error")
        return

    # Restrict environment that the code runs in
    allowed_globals["__builtins__"] = None
    locals = {"print": print}

    # Reset the turtle instance
    reset()

    # Run the turtle code
    exec(compiled, allowed_globals, locals)

    # Get the resulting image
    ts = getscreen()
    ts.getcanvas().postscript(file=file)

# Open file containing code
with open("test.txt") as file:
    code = file.read()
    run_turtle(code, "result.ps")