import argparse 
import pickle
import os
from os.path import expanduser
import sys
import json
from .todo import write, view, check


def main():
    homedir = expanduser("~")
    initfile = os.path.join(homedir,".todo.json")
    if not os.path.isfile(initfile) and sys.argv[1] != "init":
        print("Use the --init file to init")

    if sys.argv[1] == "init":
        todolist = {}
        with open(initfile, "w") as initfile:
            json.dump(todolist, initfile) 

    elif sys.argv[1] == "add" or sys.argv[1] == "a":
        project = "" 
        if len(sys.argv) > 3 and sys.argv[3] == 'p' and sys.argv[4]: 
            project = sys.argv[4]

        write(sys.argv[2], project)

    elif sys.argv[1] == "list" or sys.argv[1] == "l":
        with open(initfile) as listfile:
            data = json.load(listfile)
        view(data) 

    elif sys.argv[1] == "check" or sys.argv[1] == "c":
        with open(initfile) as listfile:
            data = json.load(listfile)
        taskidx = sys.argv[2]
        task = data[taskidx]
        modifiedTask = check(task)
        data[taskidx] = modifiedTask
        with open(initfile, "w") as initfile:
            json.dump(data, initfile)

    elif sys.argv[1] == "delete" or sys.argv[1] == "d":
        with open(initfile) as listfile:
            data = json.load(listfile)

        taskidx = sys.argv[2]
        del data[taskidx]
        with open(initfile, "w") as initfile:
            json.dump(data, initfile)
        
if __name__ == '__main__':
    main()



