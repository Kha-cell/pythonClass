from unittest import TestCase
import get_number 

class Testget_number(TestCase):
	def test_get_number_exist(self):
		get_number.get_number([11])

	def test_get_number _correct(self):
		actual = get_number.get_number([11])
		expected =[1,2,3,4,5,6,7,8,9,10,11]
		self.assertEqual(actual, expected)