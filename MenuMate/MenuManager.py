from Menu import Menu
from MenuItem import MenuItem
import sys

class MenuManager():
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.menu_stack = [main_menu]

    def run(self):
        while self.menu_stack != []:
            cur_menu = self.menu_stack.pop()
            
            prev_menu = ""
            if self.menu_stack != []:
                prev_menu = self.menu_stack[-1]
            action = cur_menu.run(prev_menu)
            
            if action == cur_menu.quit_char:
                sys.exit()
            elif action != cur_menu.back_char:
                self.menu_stack.append(cur_menu)
                if isinstance(action.func, Menu):
                    self.menu_stack.append(action.func)
                else:
                    action.run()


        # while stack is not empty
        # pop menu off stack
        # get action from menu
        # if action is not quit
            # if action is menuItem
                # push current menu back on stack
                # perform action
            # if action is a menu 
                # push current and next menu on stack
            # if action is back
                # don't put current menu back on stack
        # else
            # sys.quit 


# TODO: turn all this junk into test cases
def tester1():
    print("Whats up yooooo")

def tester2(): 
    print("Im some text")

item = MenuItem("Option 1", tester1)

menu = Menu()
menu2 = Menu("Second Menu")
menu2.add(MenuItem("Some flavor text", print))
menu3 = Menu("Third Menu")
menu2.add(menu3)
menu.add(menu3)

menu.add(item)
menu.add(MenuItem("Option 2", tester2))
menu.add(menu2) #you can either pass in a menu with a customized option text or just pass it in plain to use it's title text

menuManager = MenuManager(menu)
menuManager.run()