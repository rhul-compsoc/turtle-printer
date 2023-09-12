import curses
from ui import select_file
from interpreter import interp


# ran in curses wrapper for the stdscr.
def main(stdscr):
    selected = select_file(stdscr, 'scripts')
    # creates turtle window wth the selected file.
    interp(selected)


if __name__ == '__main__':
    curses.wrapper(main)
