# Import allowed modules
import math
from turtle import *

# Define a set of allowed functions that the user can access inside the sandbox
allowed_locals = {
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
    math,
    max,
    min,
    next,
    oct,
    ord,
    pow,
    print,
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
def run_turtle(code, canvas):
    # Compile the turtle code
    compiled = compile(code, "turtle", "exec")

    # Restrict environment that the code runs in
    allowed_globals = {"__builtins__": None}
    locals = {x.__name__: x for x in allowed_locals}

    # Create a new turtle instance and make it accessible to the sandbox
    canvas.delete("all")
    turtle = RawTurtle(canvas, shape="turtle", visible=False)
    # Move the turtle to roughly the center of the canvas
    turtle.penup()
    turtle.goto(0, -350)
    turtle.pendown()
    turtle.showturtle()
    locals["turtle"] = turtle

    # Run the turtle code
    exec(compiled, allowed_globals, locals)