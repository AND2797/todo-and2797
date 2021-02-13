from datetime import date
import argparse
import curses
import os

def createList(date):
    if not os.path.isfile(date):
        with open(f"lists/{date}.txt", 'w'):
            pass


def main(args, date):
    if args.create:
        createList(date)
    
    if args.edit:
       curses.wrapper(display, date) 


def display(stdscr, date):
    stdscr.clear()
    stdscr.timeout(500)
    maxy, maxx = stdscr.getmaxyx()
    curses.newwin(2, maxx, 3, 1)
    curses.curs_set(0)
    if (curses.has_colors()):
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
    stdscr.refresh()

    bottomBox = curses.newwin(8, maxx - 2, 1, 1)
    bottomBox.box()
    bottomBox.addstr("to-do list")
    bottomBox.refresh()
    bottomwindow = curses.newwin(6, maxx - 4, 2, 2)
    bottomwindow.addstr(date)
    bottomwindow.addstr("\n")
    bottomwindow.refresh()


    while True:
        event = stdscr.getch()
        if event == ord("q"):
            break


if __name__ == '__main__':

    date = str(date.today()) + "\n"
    if not os.path.isdir('lists'):
        os.mkdir('lists')
    parser = argparse.ArgumentParser()
    parser.add_argument("--create")
    parser.add_argument("--edit")
    args = parser.parse_args()
    main(args, date)



