# Exclude all default globals from the sandbox
disallowed = globals().copy()

# Import allowed modules
import math
from turtle import *

# Remove disallowed globals and 'disallowed' object created earlier
allowed_globals = {k: v for k, v in globals().items() if k not in disallowed and k != "disallowed"}

with open("test.txt") as file:
    code = file.read()

# Restrict environment that the code runs in
allowed_globals["__builtins__"] = None
locals = {"print": print}

# Run the turtle code
exec(code, allowed_globals, locals)

# Get the resulting image
ts = getscreen()
ts.getcanvas().postscript(file="result.ps")