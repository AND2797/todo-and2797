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
        if self.text is None:
            bottomwindow.addstr(self.name)
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
    args = parser.parse_args()

    if args.edit:
        path = os.path.join('lists/', args.edit + '.pkl')
        if not os.path.isfile(path):
            newList = todoList(args.edit)
            newList.runner()
        else:
            with open(path, 'rb') as input:
                oldList = pickle.load(input)
                oldList.runner()










