import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello my name is sayem khan and i am the best")
    stdscr.refresh()
    stdscr.getkey()  
    
wrapper(main)