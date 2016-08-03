# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: magic
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		# 测试To-Dos是否在标题中
		self.assertIn('To-Do', self.browser.title)
		head_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', head_text)

		# 邀请她输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		# 她在一个文本框中输入"buy peacock feathers"（购买孔雀羽毛）
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1:Buy peacock features' for row in rows)
		)

		# 页面中又显示了一个文本框，可以输入其他代办事项
		# 她输入 use peacock feature to make a fly
		self.fail('Finish the test')

if __name__ == '__main__':
	unittest.main()
