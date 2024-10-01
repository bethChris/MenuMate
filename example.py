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