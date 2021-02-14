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

<p align = "center">
    <img src = https://i.imgur.com/k4Os5yX.png>
</p>

## Installation
Clone the repository

`git clone https://github.com/AND2797/todo.git`

`cd todo`

Move the python file to /usr/bin
```
sudo mv todo.py /usr/bin/todo
```

## Usage

### Create / Edit a new list:
```python
todo --edit <listname>
# creates a new to-do list with <listname> or opens an existing to-do list with <listname>
```

### Delete lists:
```python
todo --remove all
# removes all to-do lists

todo --remove <listname>
# deletes a to-do list
```
