# Import allowed modules
import math
from turtle import *

# Define a set of allowed functions that the user can access inside the sandbox
allowed_globals = {
    abs,
    aiter,
    all,
    anext,
    any,
    ascii,
    bin,
    bool,
    bytearray,
    bytes,
    chr,
    dict,
    divmod,
    enumerate,
    filter,
    float,
    format,
    hash,
    hex,
    iter,
    len,
    list,
    map,
    max,
    min,
    next,
    oct,
    ord,
    pow,
    range,
    repr,
    reversed,
    round,
    set,
    slice,
    sorted,
    str,
    sum,
    tuple,
    type,
    zip
}

# run_turtle runs the given code and displays the result on the given canvas
# print_func specifies a function to use in place of print when running user code
def run_turtle(code, canvas, print_func=print):
    # Compile the turtle code
    compiled = compile(code, "turtle", "exec")

    # Restrict environment that the code runs in
    globs = {"__builtins__": {x.__name__: x for x in allowed_globals}, "math": math}

    # Create a new turtle instance and make it accessible to the sandbox
    canvas.delete("all")
    turtle = RawTurtle(canvas, shape="turtle", visible=False)
    # Move the turtle to roughly the center of the canvas
    turtle.penup()
    turtle.goto(0, -350)
    turtle.pendown()
    turtle.showturtle()
    globs["turtle"] = turtle
    
    # Give overridden print function
    globs["__builtins__"]["print"] = print_func

    # Run the turtle code
    exec(compiled, globs, {})