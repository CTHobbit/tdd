from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob thinks that he needs a new to-do app, so he goes to
        self.browser.get('http://localhost:8000')

        # He notices that the page title and header indicate a to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        

# The first thing he sees is the option to enter a to-do item

# He types "Buy turkey feathers" into a text box (Bob collects feathers from molting birds)

# When he hits enter, the page updates, and now the page lists
# "1: Buy turkey feathers" as an item in a to-do list

# There is still a text box inviting him to add more items
# He enters "use turkey feathers to make a fan" (Bob is very creative)

# The page updates again, and now shows both items on the list

# Bob wonder whether the site will remember the list
# Then he sees that the site has generated a unique URL for him, and there is some
# explanatory text describing that

# He visits the URL, the to-do list is still there

# Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')