from unittest import TestCase
import get_even

class Testsum_even(TestCase):
	def test_that_get_even_exist(self):
		get_even.get_even([2,7,9,17,19,2,8,10])

	def test_that_get_even_correct(self):
		actual = get_even.get_even([2,7,9,17,19,2,8,10])
		expected = 22
		self.assertEqual(actual, expected)