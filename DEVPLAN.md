# Software Development Plan

## Design

Goal: a library that allows easy creation of a simple terminal menu, with advanced options to customize multiple features such as style, chaining menus and input validation.

MVP: a library that will allow a quick boot up of a simple, clean looking terminal menu 

MVP+: input validations

MVp++: chaining menus

MVP+++: style


#### Tools Needed:

- `inspect` module for extracting the names of params of python functions (for input validation in input menu items)


### Plan:
`Menu`: 

    - MenuItems[]
    - Title
    - Add()
    - Selection() 
    - Run()

Menu is in charge of running the selection loop. Displaying the menu and collecting user input, then calling a MenuItem's run method to begin whatever process is linked with the item.

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

`MenuManager`: 

    - main_menu > Menu object for the root menu
    - history[] > Menu object stack of Menus that we have previously visted
    - Run() > runs the main loop as long as the stack of menus is not empty


MenuManager is in charge of running the main menu loop and invoking MenuItem functions. It will run the menu that is currently at the top of the history stack. It recieves the selection from the Menu its currently running, validates its not 'break' or 'quit' (which require special intervention) and then runs the selected MenuItem if everythings solid.



```python
class MenuManager():
    def __init__(self, main_menu):
        main_menu = the start menu
        history = stack of menus (main menu is first)
    
    def run(self):
       while stack is not empty
        pop menu off stack
        get action from menu
        if action is not quit
            if action is menuItem
                push current menu back on stack
                perform action
            if action is a menu 
                push current and next menu on stack
            if action is back
                dont put current menu back on stack
        else
            sys.quit 

```

### Menu Implementation
You can build a Menu by defining a new Menu object and calling the menus add() method by passing in a MenuItem, which contains a text desription and an associated runnable. If you want to pass along another Menu as an option (to navigate to a new menu on a selection), you can pass in a Menu object itself as the function in the MenuItem object. 

EXAMPLE USAGE: 
```python
### CUSTOM FUNCTIONS ###
def tester1():
    print("Whats up yooooo")

def tester2(): 
    print("Im some text")

### TURNING FUNCTIONS INTO MENUITEMS ###
testing1 = MenuItem("Yo", tester1)
testing2 = MenuItem("text", tester2)

### SETTING UP MENU OBJECTS ###
main_menu = Menu("Main Menu")
second_menu = Menu("Second Menu")

### ADDING NORMAL MENUITEMS INTO EACH MENU ###
main_menu.add(testing1)
second_menu.add(testing2)

### ADDING SECOND MENU TO MAIN MENU ###
second_menu_option = MenuItem("Epic Second Menu", second_menu)
main_menu.add(second_menu_option)

### PASSING MAIN MENU TO MENU MANAGER OBJECT ###
menu_manager = MenuManager(main_menu)

### RUN MENU MANAGER ###
menu_manager.run() 
```

## File Structure

`__init__.py` - for setuptools

`Menu.py` - for the Menu object which contains menuItems and built in selection validation

`MenuItem.py` - for the MenuItem object which contains the selection text and the associated function

`MenuManager.py` - the main driving class, contains menus and tracks history of menus


## Implementation Notes
- I'm gonna need to learn how to call **handler functions** for the functionality I want to incorporate
- setuptools require a `setup.py` with the package information to work
- the code is split into 3 objects, splitting the functionality of the original `Menu` object into `Menu` and `MenuManager`.
- `MenuManager` will be the main controller of the selections and keeping track of the chaining menus.
- chaining Menus with history memory will work as long as there is no reference to a previous menu in a menu down the line. There's a "history" of where the user was last that the `MenuManager` will keep track of (via a stack). And a "back" button is included on Menus traveled to from another menu

## Unit Testing
For creating the unit tests, I'm focusing on testing small pieces of the functionality for each class. The major concerns are the checks in the Menu class and the implementation of input options in the MenuItem class that I'll be adding later. 

As for the MenuItem and MenuManager classes as they are I'm struggling to find things to test for those. Currently I have tests ensuring the initialization of each class works but those might be removed later as I don't know if those are necessariily needed.
