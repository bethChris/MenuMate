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
second_menu_option = MenuItem(text="Show Me The Second Menu", func=second_menu)

### ADDING ANOTHER MENU ITEM TO MAIN_MENU ###
main_menu.add(menu_item=second_menu_option)

### SETTING UP A MENU MANAGER OBJECT ###
# pass your main menu into the menu manager #
menu_manager = MenuManager(main_menu=main_menu)

### RUN MENU MANAGER ###
menu_manager.run()

# from MenuMate import MenuItem, Menu, MenuManager

# ### CUSTOM FUNCTIONS ###
# # You write these #
# def ask_whats_up():
#     print("What's up? How was your day?")

# def hello_world(): 
#     print("Hello World!")

# ### TURNING YOUR FUNCTIONS INTO MENU ITEMS ###
# option_1 = MenuItem("Ask Me What's Up", ask_whats_up)
# option_2 = MenuItem("Say Hello", hello_world)

# ### SETTING UP A MENU OBJECT ###
# main_menu = Menu("Main Menu")

# ### ADDING MENU ITEMS INTO A MENU ###
# main_menu.add(option_1)
# main_menu.add(option_2)

# ### SETTING UP A MENU MANAGER OBJECT ###
# # pass your main menu into the menu manager #
# menu_manager = MenuManager(main_menu)

# ### RUN MENU MANAGER ###
# menu_manager.run() 

