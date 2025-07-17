import curses
from curses import wrapper
import time 
import random

def start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to typewar")
    stdscr.addstr("\nPress any key to start!")
    stdscr.refresh()
    stdscr.getkey()
    

def load_txt():
    with open("typewar.txt", "r") as file: 
        lines = file.readlines()
        return random.choice(lines).strip()

def start_test(stdscr , target , user , wpm):
    correct_txt = []
    stdscr.addstr(target)
    stdscr.addstr(1 , 0 , f"WPM: {wpm}")
    for i , char in enumerate(user):
        correct_txt = target[i]
        color = curses.color_pair(1)
        if correct_txt != char :
            color = curses.color_pair(2)
        stdscr.addstr(0 , i , char , color)

def test(stdscr):
    target_txt =  load_txt()
    user_txt = []
    wpm = 0
    start = time.time()
    stdscr.nodelay(True)
    while True:
        time_passed = max(time.time() - start , 1)
        wpm = round((len(user_txt) / (time_passed / 60)) / 5 )

        stdscr.erase()
        start_test(stdscr,target_txt , user_txt , wpm)
        stdscr.refresh()

        if "".join(user_txt) == target_txt :
            break
        try : 
            key = stdscr.getkey()
        except:
            continue
        try :
            if ord(key) == 27: 
                break
            if key in ("KEY_BLACKSPACE" , "\b" , "\x7f"):
                try:
                    if len(key) > 0 :
                        user_txt.pop()
                except: 
                    continue
            elif len(user_txt) < len(target_txt) : 
                user_txt.append(key)
        except : 
            continue

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_RED , curses.COLOR_BLACK)
    curses.init_pair(3 , curses.COLOR_YELLOW , curses.COLOR_BLACK)
    start(stdscr)
    while True : 
        test(stdscr)
        stdscr.nodelay(False)
        stdscr.addstr(2 , 0 , "You have completed the text! Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27 :
            break 

wrapper(main)