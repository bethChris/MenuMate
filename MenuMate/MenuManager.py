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


# TODO: turn all this junk into test cases
def tester1():
    print("Whats up yooooo")

def tester2(): 
    print("Im some text")

testing1 = MenuItem("Yo", tester1)
testing2 = MenuItem("text", tester2)
testing3 = MenuItem("Option", print)

main_menu = Menu("Main Menu")
main_menu.add(testing3)

second_menu = Menu("Second Menu")
second_menu.add(testing1)
second_menu.add(testing2)

main_menu.add(MenuItem("Fun Times Menu", second_menu))

menuManager = MenuManager(main_menu)
menuManager.run()