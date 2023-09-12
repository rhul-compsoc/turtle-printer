import os
import curses


# list all files in a given directory.
def list_files(stdscr, directory, selected_index):
    stdscr.clear()
    # hidden files should not be visible and only files ending in .tpy should be runnable.
    files = [file for file in os.listdir(directory) if not file.startswith('.') and file.endswith('.tpy')]
    # show the files.
    for i, file in enumerate(files):
        if i == selected_index:
            stdscr.addstr(i, 0, f"> {file}", curses.A_REVERSE)
        else:
            stdscr.addstr(i, 0, f"  {file}")
    stdscr.refresh()


# select a given file from a given directory.
def select_file(stdscr, directory):
    # hidden files should not be visible and only files ending in .tpy should be runnable.
    files = [file for file in os.listdir(directory) if not file.startswith('.') and file.endswith('.tpy')]
    selected_index, key = 0, 0

    try:
        while key != ord('\n'):  # enter key
            stdscr.clear()
            list_files(stdscr, directory, selected_index)

            key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = max(0, selected_index - 1)
            elif key == curses.KEY_DOWN:
                selected_index = min(len(files) - 1, selected_index + 1)

        # when a file is selected get the path and selected file to return path to file
        selected_file = os.path.join(directory, files[selected_index])
        return selected_file
    finally:
        curses.endwin()  # close the curses window
