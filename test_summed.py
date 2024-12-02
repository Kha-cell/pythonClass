from unittest import TestCase 
import  summed

class TestSummed(TestCase):
	def test_summedfunction_exist(self):
		summed.get_sum([1,2,3])

def test_that_summedfunction_correct(self):
	actual = summed.get_sum([1,2,3])
	expected = [2,4,6]
	self.assertEqual(actual, expected)