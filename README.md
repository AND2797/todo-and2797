# todo

```
+-----------------+ 
| > +--todo----+  | 
|   | 1.       |  | 
|   | 2.       |  | 
|   +----------+  | 
+-----------------+ 
```

Minimalist to-do list to incorporate in your terminal workflow. 

## Why?

GUI to-do lists are distracting, moreover often you might not have access to
GUIs and may want to make small notes or keep track of tasks in a CLI.

Modern to-do lists are highly sophisticated, and I often found myself over-organizing
with categories / labels etc. I needed a simple way (without much window switching) way to keep track of my tasks.



## Installation

### *nix

Move the python file to /usr/bin
```
sudo mv todo.py /usr/bin/todo.py
```

### Windows

## Usage

### Create / Edit a new list:
```python
python3 todo.py --edit <listname>
# creates a new to-do list with <listname> or opens an existing to-do list with <listname>
```

### Delete lists:
```python
python3 todo.py --remove all
# removes all to-do lists

python3 todo.py --remove <listname>
# deletes a to-do list
```
