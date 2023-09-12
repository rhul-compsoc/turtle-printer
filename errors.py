class UserSyntaxError(SyntaxError):
    def __init__(self, linenum, offset, text, msg):
        # Create a nice looking syntax error without a stacktrace
        super().__init__(f"Your code contains a syntax error:\nError on line {linenum}, col {offset}:\n> {text}\n{' ' * (offset + 1)}^\n{msg}")


class UserRuntimeError(Exception):
    def __init__(self, error):
        self.error = error
        super().__init__(error)
