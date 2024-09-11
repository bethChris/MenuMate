# Software Development Plan

## Design

Goal: a library that allows easy creation of a simple terminal menu, with advanced options to customize multiple features such as style, chaining menus and input validation.

MVP: a library that will allow a quick boot up of a simple, clean looking terminal menu 

MVP+: input validations

MVp++: chaining menus

MVP+++: style


### Plan:
`Menu`: 

    - MenuItems[]
    - Title
    - Add()
    - Selection() 
    - Run()

Menu is in charge of running the selection loop. Displaying the menu and collecting user input, then calling a MenuItem's run method to begin whatever process is linked with the item.

#### Tools Needed:

- `inspect` module for extracting the names of params of python functions (for input validation in input menu items)


```python

class Menu():
    def __init__(title="Menu")
        self.menu_items = []
        self.title = title
        self.previous_menu
    
    def add(menu_item):
        if the menu_item is another menu
            this means weve added
        self.menu_items.insert(menu_item)

    def run():
        # descrs = [m.text for m in self.menu_items]
        # options = [i for i in range(len(menu_items))]
        # longest_descr = max(len(max(descrs, key=len)), len(title))
        # longest_opt = len(max(options, key=len)) + 3
        # print()
        # print(f"{self.title:^{longest_descr+longest_opt}}")

        # print("-"*(longest_descr+longest_opt))
        # for opt, descr in zip(options, descrs):
        #     print(f"[{opt}] {descr}")
        # print("-"*(longest_descr+longest_opt))
        # print()

        take input from user
            only accept input from options list
            

```


`MenuItem`: 

    - Text
    - Run() > linked to function


MenuItem will be in charge of running itself and including any input validation that we may add later for running their respective functions.

```python

class MenuItem():
    def __init__(text, func, takes_input=False, chaining=False):
        self.text = text
        self.func = func

    def run():
        if takes_input:
            for each param in self.func
                prompt for input
                save input

        try/catch     
            call function (with input if applicable)

        if fail to run function (wrong input type or other)
            run some sort of error message and ask if redo or exit
        
            if redo, 
                call run again, 
            else 
                let method end and return to menu

    def gather_input():
        # if input gathering is too large, maybe add it here for readability

```


## Structure

`__init__.py` - for setuptools

`Menu.py` - for the Menu object

`MenuItem.py` - for the MenuItem object

