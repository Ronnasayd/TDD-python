from selenium import webdriver
import os
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.browser = webdriver.Chrome(self.path+'/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
