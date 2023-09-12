from errors import UserRuntimeError, UserSyntaxError
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

# run_turtle runs the given code and exports the resulting turtle image to the given file
def run_turtle(code, canvas):
    # Compile the turtle code
    try:
        compiled = compile(code, "turtle", "exec")
    except SyntaxError as e:
        raise UserSyntaxError(e.lineno, e.offset, e.text, e.msg) from e

    # Restrict environment that the code runs in
    allowed_globals = {"__builtins__": None}
    locals = {x.__name__: x for x in allowed_locals}

    # Create a new turtle instance and make it accessible to the sandbox
    canvas.delete("all")
    turtle = RawTurtle(canvas)
    locals["turtle"] = turtle

    # Run the turtle code
    try:
        exec(compiled, allowed_globals, locals)
    except Exception as e:
        raise UserRuntimeError(e) from e