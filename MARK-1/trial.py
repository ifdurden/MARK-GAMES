import curses
from curses import wrapper
def main(stdscr):
    stdscr.clear()
    stdscr.addstr("hello my name is sayem khan and i am a mechanic")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)