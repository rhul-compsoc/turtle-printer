class UserSyntaxError(SyntaxError):
    def __init__(self, linenum, offset, text, msg):
        super().__init__(f"Your code contains a syntax error:\nError on line {linenum}, col {offset}:\n> {text}\n{' ' * (offset + 1)}^\n{msg}")


class UserRuntimeError(RuntimeError):
    pass
