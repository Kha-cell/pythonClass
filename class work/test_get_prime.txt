from unittest import TestCase
import get_prime

class Testsum_prime(TestCase):
	def test_that_get_prime_exist(self):
		get_prime.get_prime([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

	def test_that_get_prime_correct(self):
		actual = get_prime.get_prime([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
		expected =2,5,7,11,13,17,19,
		self.assertEqual(actual, expected)