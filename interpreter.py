from errors import UserRuntimeError, UserSyntaxError


# Exclude all default globals from the sandbox
disallowed = globals().copy()


# Import allowed modules
import math
from turtle import *


# Remove disallowed globals and 'disallowed' object created earlier
allowed_globals = {k: v for k, v in globals().items() if k not in disallowed and k != "disallowed"}


# Define a set of allowed builtin functions that the user can access inside the sandbox
allowed_builtins = {
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
def run_turtle(code, file):
    # Compile the turtle code
    try:
        compiled = compile(code, "turtle", "exec")
    except SyntaxError as e:
        raise UserSyntaxError(e.lineno, e.offset, e.text, e.msg) from e

    # Restrict environment that the code runs in
    allowed_globals["__builtins__"] = None
    locals = {x.__name__: x for x in allowed_builtins}

    # Reset the turtle instance
    reset()

    # Run the turtle code
    exec(compiled, allowed_globals, locals)

    # Get the resulting image
    ts = getscreen()
    ts.getcanvas().postscript(file=file)


# Run the program
def interp(file="test.txt"):
    # Open file containing code
    with open(file) as file:
        code = file.read()
        try:
            run_turtle(code, "result.ps")
        except UserSyntaxError as e:
            print(e)
