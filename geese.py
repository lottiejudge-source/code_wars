import unittest

class Geese_Removal_Test(unittest.TestCase):
    def test_geese_exist(self):
        self.assertIsInstance(geese, list)
    
    def test_removal_of_geese(self):
        birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
        expected = ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
        result = geese_removal_function(birds)
        self.assertListEqual(result, expected)
    
    def test_no_geese_in_list(self):
        birds = ["Mallard", "Hook Bill", "Crested"]
        expected = ["Mallard", "Hook Bill", "Crested"]
        result = geese_removal_function(birds)
        self.assertListEqual(result, expected)

    
    


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def geese_removal_function(birdArray):
    geese_removed = [bird for bird in birdArray if bird not in geese]

    return geese_removed



if __name__ == '__main__':
    unittest.main()


# the rules 
# Write a function that takes a list of strings as an argument and 
# returns a filtered list containing the same elements but with the 'geese' removed.