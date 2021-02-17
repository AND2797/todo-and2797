from datetime import date
import pickle
import argparse
import curses
import curses.textpad
import os



class todoList:
    def __init__(self, name, settings):
        self.name = name
        self.text = None
        self.settings = settings 

    def runner(self):
        curses.wrapper(self.display)
       
    def _save(self):
        with open(f"{self.settings['save_loc']}/{self.name}.pkl", 'wb') as output:
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

