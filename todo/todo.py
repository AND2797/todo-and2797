import sys
from os.path import expanduser
import os
import json

homedir =  expanduser("~")
initfile = os.path.join(homedir,".todo.json")

def opentodo(filepath):
    with open(filepath) as todolist:
        data = json.load(todolist)
    return data

def writetodo(filepath, data):
    with open(filepath, "w") as todolist:
        json.dump(data, todolist)

def write(txt, project = None):
    data = opentodo(initfile)
    newid = len(data) + 1
    data[newid] = {}
    data[newid]["txt"] = txt 
    data[newid]["done"] = False
    data[newid]["project"] = project
    writetodo(initfile, data)

def view(todolist):
    for key, value in todolist.items():
        render(key, value)

def render(idx, item):
    donebox = '[ ]' if item["done"] is False else '[x]'
    print(f"{idx} {donebox} {item['txt']} {item['project']}")


def check(taskdata):
    taskdata["done"] = True
    return taskdata



    





    
    




