from unnittest import TestCase 
import  get_sum 

class Test_get_sum(TestCase):
	def test_get_sumfunction_exist(self):
		get_sum.get_sum([1,2,3])

def test_get_sumfunction_correct(self):
	actual = get_sum.get_sum([1,2,3])
	expected = [2,4,6]
	self.assertEqual(actual, expected)