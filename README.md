# todo

```
+-----------------+ 
| > 1. [ ] task1  |
|   2. [x] task2  |
|                 | 
|                 | 
|                 | 
+-----------------+ 
```

Minimalist to-do list to incorporate in your terminal workflow. 

## Why?

GUI to-do lists are distracting, moreover often you might not have access to
GUIs and may want to make small notes or keep track of tasks in a CLI.

Modern to-do lists are highly sophisticated, and I often found myself over-organizing
with categories / labels etc. I needed a simple way (without much window switching) way to keep track of my tasks.

Initially set out to create a TUI but since I've been inspired to create a simple version of ultralist (https://github.com/ultralist) 
as it follows a very clean and easy to work with design. 

<p align = "center">
    <img src = https://i.imgur.com/k4Os5yX.png>
</p>

## Installation
```
pip install todo-and2797
```

## Usage
### todo init:
todo uses a `.todo.json` file as persistant storage for lists in `json` format. At the moment the file is created in the home directory of the user.

```
todo init
```

### Add a new task:
```python
todo a <task> 
# adds a new task to the list

todo a <task> p <project>
# adds a new task under a specific project
```
### Complete a task:
```python
todo c <task number>
# marks the task as done with a [x]
```

### View current list:
```python
todo l
# prints all to-do lists.
```
### Delete task:
```python
todo d "all" 
# removes all tasks from the list 

todo d <task number> 
# deletes a specific task 
```

