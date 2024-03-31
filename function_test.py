from selenium import webdriver

import unittest


class NewVistorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do',self.browser.title), "broswer title was " + self.browser.title

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()


# broswer = webdriver.Chrome()

# broswer.get('http://localhost:8000')

# assert 'T' in broswer.page_source
