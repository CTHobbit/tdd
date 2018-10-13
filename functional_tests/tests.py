from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob thinks that he needs a new to-do app, so he goes to
        self.browser.get(self.live_server_url)

        # He notices that the page title and header indicate a to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('To-Do', header_text)
        

        # The first thing he sees is the option to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy turkey feathers" into a text box (Bob collects feathers from molting birds)
        inputbox.send_keys('Buy peacock feathers')  

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy turkey feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')  

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly" (Bob is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Bob wonders whether the site will remember his list. Then she sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # He visits that URL - his to-do list is still there.

# The page updates again, and now shows both items on the list

# Bob wonder whether the site will remember the list
# Then he sees that the site has generated a unique URL for him, and there is some
# explanatory text describing that

# He visits the URL, the to-do list is still there

# Satisfied, he goes back to sleep

#if __name__ == '__main__':
#    unittest.main(warnings='ignore')
#removed per chapter 6