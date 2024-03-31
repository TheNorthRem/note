from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest
import time

class NewVistorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do',self.browser.title), "broswer title was " + self.browser.title

		header_test = self.browser.find_element(By.TAG_NAME,'h1').text

		self.assertIn('To-Do',header_test)

		input_box = self.browser.find_element(By.ID,'id_new_item')

		self.assertEqual(input_box.get_attribute('placeholder'),
				   'Enter a to-do item')
		
		input_box.send_keys('Buy flowers')

		input_box.send_keys(Keys.Enter)

		time.sleep(1)

		table = self.browser.find_element(By.ID,'id_list_table')
		rows = table.find_element(By.TAG_NAME,'tr')

		self.assertIn('1: Buy flowers', [row.text for row in rows])

	

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()

