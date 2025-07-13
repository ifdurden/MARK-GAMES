import curses
from curses import wrapper

def main (srdscr):
    stdscr.clear()
    stdscr.addstr("Hello my name is sayem khan and i am the best of then all")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)