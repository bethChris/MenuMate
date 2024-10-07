from MenuMate import MenuItem, Menu, MenuManager

### CUSTOM FUNCTIONS ###
# You write these #
def a_simple_lad():
    print("Salt is spicy")
    
def peak_musical_genius():
    print("Ring-ding-ding-ding-dingeringeding!")

### SETTING UP MENU OBJECTS ###
main_menu = Menu(title="Main Menu")
second_menu = Menu(title="Nifty Second Menu")

### TURNING YOUR FUNCTIONS INTO MENU ITEMS ###
option_1 = MenuItem(text="Hot Take", func=a_simple_lad)
option_2 = MenuItem(text="What Does the Fox Say?", func=peak_musical_genius)

### ADDING MENU ITEMS INTO THE MENUS ###
main_menu.add(menu_item=option_1)
second_menu.add(menu_item=option_2)

### TURNING A MENU INTO A MENU ITEM ###
# the ~advanced~ part of this example #
second_menu_option = MenuItem(text="Show Me The Second Menu", func=second_menu)

### ADDING ANOTHER MENU ITEM TO MAIN_MENU ###
main_menu.add(menu_item=second_menu_option)

### SETTING UP A MENU MANAGER OBJECT ###
# pass your main menu into the menu manager #
menu_manager = MenuManager(main_menu=main_menu)

### RUN MENU MANAGER ###
menu_manager.run()