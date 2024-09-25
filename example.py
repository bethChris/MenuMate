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