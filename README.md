# ConsoleMenu
A simple console menu for Python3.x scripts

## How to
All you need to do is to use dictionaries to define the structure of your menu.
You're able to use functions and other menus as items, so you can build an infinitive nested menu.
Then call **execute** method and that's it!

```python
from consolemenu import ConsoleMenu

def func1():
    # Your code here

def func2():
    # Your code here

def func3():
    # Your code here

nested_menu = ConsoleMenu(
    "Sample nested menu",
    {
        "call func1": func1,
        "call func2": func2,
        "call func3": func3,
    }
)

menu = ConsoleMenu(
    "Sample menu",
    {
        "call func1": func1,
        "call func2": func2,
        "call func3": func3,
        "goto nested menu": nested_menu,
    }
)

menu.execute()
```

The output will be:
```
Sample menu
1) call func1
2) call func2
3) call func3
4) goto nested menu
5) exit
run:
```
