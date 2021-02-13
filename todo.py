from datetime import date
import pickle
import argparse
import curses
import curses.textpad
import os

class todoList:
    def __init__(self, name):
        self.name = name

    def runner(self):
        curses.wrapper(self.display)
    
    def display(self, stdscr):
        stdscr.clear()
        stdscr.timeout(500)
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
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
        bottomwindow.addstr(self.name)
        bottomwindow.addstr("\n")
        tb = curses.textpad.Textbox(bottomwindow)
        text = tb.edit()
        bottomwindow.refresh()



        while True:
            event = stdscr.getch()
            if event == ord("q"):
                break

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--edit")
    args = parser.parse_args()

    if args.edit:
        if not os.path.isfile(args.edit + '.pkl'):
            newList = todoList(args.edit)
            newList.runner()










