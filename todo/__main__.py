import argparse 
import os
import json
from .todo import todoList

def main(args):
    if not os.path.isfile('./settings.json'):
        print("settings.json file not found. Please set it using --settings flag")
        #exit
    else:
        with open('./settings.json', 'r') as settingsFile:
            settings = json.load(settingsFile)

    dirpath = settings["save_loc"]
    if args.settings:
        settings = {}
        settings["save_loc"] = str(input("Save path:"))
        with open("./settings.json", "w") as settingsFile:
            json.dump(settings, settingsFile)

    if args.edit:
        path = os.path.join(dirpath, args.edit + '.pkl')
        if not os.path.isfile(path):
            newList = todoList(args.edit, dirpath)
            newList.runner()
        else:
            with open(path, 'rb') as input:
                oldList = pickle.load(input)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--edit")
    parser.add_argument("--remove")
    parser.add_argument("--settings")

    args = parser.parse_args()
    main(args)



