import unittest
from MenuMate import MenuItem, Menu, MenuManager

# test functions to use in testcases
def test_func_1():
    print("Whats up yooooo")

def test_func_2(): 
    print("Im some text")

class MenuItemTestCase(unittest.TestCase):
    pass

class MenuTestCase(unittest.TestCase):
    def setUp(self):
        self.menu = Menu("First Menu")
        self.second_menu = Menu("Second Menu")
    
    def test_adding_valid_menu_item(self):
        test_item = MenuItem("Option 1", test_func_1) # should have already passed tests
        try:
            self.menu.add(test_item)
        except Exception as e:
            self.fail(f"Code raised an exception unexpectedly: {e}")
    
    def test_adding_valid_menu(self):
        second_menu_item = MenuItem("Second Menu", self.second_menu)
        try:
            self.menu.add(second_menu_item)
        except Exception as e:
            self.fail(f"Code raised an exception unexpectedly: {e}")
        
    def test_adding_invalid_menu(self):
        # test for type error if anything but a MenuItem is added
        with self.assertRaises(TypeError):
            self.second_menu.add(self.menu)
        
        with self.assertRaises(TypeError):
            self.second_menu.add("Option #1")

        with self.assertRaises(TypeError):
            self.second_menu.add(test_func_1)
        
        # should have already passed previous tests
        first_menu_item = MenuItem("First Menu", self.menu)
        self.second_menu.add(first_menu_item)
        second_menu_item = MenuItem("Second Menu", self.second_menu)
        
        # test for value error if menu references itself or previous menus
        with self.assertRaises(ValueError):
            self.menu.add(first_menu_item)
            
        with self.assertRaises(ValueError):
            self.menu.add(second_menu_item)

            
class MenuManagerTestCase(unittest.TestCase):
    pass