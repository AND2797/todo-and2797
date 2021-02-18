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
```
pip install todo-and2797
```

## Usage
### Create a settings file:
When using for the first time a settings file needs to be initialized, which contains the path
to the folder where you want your saved lists to be saved.
```
todo --settings 1
```

### Create / Edit a new list:
```python
todo --edit <listname>
# creates a new to-do list with <listname> or opens an existing to-do list with <listname>
```
### View current lists:
```python
todo --view 1
# prints all to-do lists.
```
### Delete lists:
```python
todo --remove all
# removes all to-do lists
```
todo --remove <listname>
# deletes a to-do list
```

### Keybinds
```
^G - Exit editing mode.
q  - Quit todo
```
