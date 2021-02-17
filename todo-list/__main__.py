import argparse 
import pickle
import os
import sys
import json
from .todo-list import todoList

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--edit")
    parser.add_argument("--remove")
    parser.add_argument("--settings")
    args = parser.parse_args()


    settingsPath = os.path.join(os.path.split(sys.executable)[0], 
                            'settings.json')
    if args.settings:
        settings = {}
        saveLoc = str(input("Save path for lists:"))
        settings["save_loc"] = os.path.join(saveLoc,'saved_lists')
        os.makedirs(settings["save_loc"], exist_ok = True)
        with open(settingsPath, "w") as settingsFile:
            json.dump(settings, settingsFile)
    else:
        if not os.path.isfile(settingsPath):
            print("settings.json file not found. Please set it using --settings flag")
            sys.exit()
        else:
            with open(settingsPath, 'r') as settingsFile:
                settings = json.load(settingsFile)

    dirpath = settings["save_loc"]
    if args.edit:
        path = os.path.join(dirpath, args.edit + '.pkl')
        if not os.path.isfile(path):
            newList = todoList(args.edit, settings)
            newList.runner()
        else:
            with open(path, 'rb') as inputList:
                oldList = pickle.load(inputList)
                oldList.runner()

    elif args.remove:
        if args.remove == 'all':
            files = os.listdir(dirpath)
            for _ in files:
                path = os.path.join(dirpath, _)
                os.remove(path)
            print("Removed all lists.")
        else:
            path = os.path.join(dirpath, args.remove + '.pkl')
            if os.path.isfile(path):
                os.remove(path)
                print(f"Removed {args.remove}")
            else:
                print("File does not exist.")





if __name__ == '__main__':
    main()



