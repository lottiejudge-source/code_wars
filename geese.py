import unittest

class Geese_Removal_Test(unittest.TestCase):
    def test_geese_exist(self):
        self.assertIsInstance(geese, list)
    
    def test_removal_of_geese(self):
        self.assertListEqual(non_geese, geese_removed)


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

non_geese = ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

geese_removed = ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]


if __name__ == '__main__':
    unittest.main()


# the rules 
# Write a function that takes a list of strings as an argument and 
# returns a filtered list containing the same elements but with the 'geese' removed.