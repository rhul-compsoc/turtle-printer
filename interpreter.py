import math

code = "print(math.sqrt(4))"

# Restrict environment that the code runs in
globals = {"__builtins__": None, "math": math}
locals = {"print": print}

exec(code, globals, locals)