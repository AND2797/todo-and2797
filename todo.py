#!/usr/bin/env python3
#!/usr/bin/env python
from datetime import date
import pickle
import argparse
import curses
import curses.textpad
import os

class todoList:
    def __init__(self, name):
        self.name = name
        self.text = None

    def runner(self):
        curses.wrapper(self.display)
       
    def _save(self):
        with open(f"lists/{self.name}.pkl", 'wb') as output:

            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
    
    def display(self, stdscr):
        stdscr.clear()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        maxy, maxx = stdscr.getmaxyx()
        curses.newwin(2, maxx, 3, 1)
        curses.curs_set(1)
        stdscr.refresh()
        bottomBox = curses.newwin(20, 30, 1, 1)
        bottomBox.box()
        bottomBox.addstr("todo")
        bottomBox.refresh()
        bottomwindow = curses.newwin(18, 28 , 2, 2)
        if self.text is None:
            bottomwindow.addstr(self.name + ' ')
            bottomwindow.addstr(date.today().strftime('%m-%d-%Y'))
            bottomwindow.addstr("\n")
            tb = curses.textpad.Textbox(bottomwindow)
            text = tb.edit()
            self.text = text
            self._save()
            bottomwindow.refresh()
        else:
            bottomwindow.addstr(self.text)
            tb = curses.textpad.Textbox(bottomwindow)
            text = tb.edit()
            self.text = text
            self._save()
            bottomwindow.refresh()

        while True:
            event = stdscr.getch()
            if event == ord("q"):
                break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--edit")
    parser.add_argument("--remove")
    args = parser.parse_args()
    dirpath = os.path.join(os.getcwd(),'todo_lists')
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    if args.edit:
        path = os.path.join(dirpath, args.edit + '.pkl')
        if not os.path.isfile(path):
            newList = todoList(args.edit)
            newList.runner()
        else:
            with open(path, 'rb') as input:
                oldList = pickle.load(input)
                oldList.runner()

    elif args.remove:
        if args.remove == 'all':
            files = os.listdir(dirpath)
            for _ in files:
                path = os.path.join(dirpath,_)
                os.remove(path)
            print("Removed all lists.")
        else:
            path = os.path.join(dirpath, args.remove + '.pkl')
            if os.path.isfile(path):
                os.remove(path)
                print(f"Removed {args.remove}")
            else:
                print("File does not exist.")












