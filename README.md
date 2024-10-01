# Menu Mate
Tired of spending way too much time setting up terminal menu's instead of just getting into making the code? Well I was, so I took all my old code used for making menu's in my college courses and made this python library. 

You're welcome I guess.

# What Do It Do?
Great question. Here's a simple example of what this code does:

```python
from MenuMate import MenuItem, Menu, MenuManager

### CUSTOM FUNCTIONS ###
# You write these #
def ask_whats_up():
    print("What's up? How was your day?")

def hello_world(): 
    print("Hello World!")

### TURNING YOUR FUNCTIONS INTO MENU ITEMS ###
option_1 = MenuItem("Ask Me What's Up", ask_whats_up)
option_2 = MenuItem("Say Hello", hello_world)

### SETTING UP A MENU OBJECT ###
main_menu = Menu("Main Menu")

### ADDING MENU ITEMS INTO A MENU ###
main_menu.add(option_1)
main_menu.add(option_2)

### SETTING UP A MENU MANAGER OBJECT ###
# pass your main menu into the menu manager #
menu_manager = MenuManager(main_menu)

### RUN MENU MANAGER ###
menu_manager.run() 
```
This code runs:

![Screenshot of code output in the terminal. Displays a menu with 2 options and a quit option. ](images/MenumateEx1.jpg "Code Output")
