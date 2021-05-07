import doctest
import unittest

def BubbleSort(arr):
	"""
	DocTest List Bubble Sort
	>>> BubbleSort([])
	[]
	>>> BubbleSort([2,1,3]) # doctest: +NORMALIZE_WHITESPACE
	[1, 2, 3]
	"""
	for i in range(len(arr) - 1):
		for j in range(len(arr) - i - 1):
			if int(arr[j]) > int(arr[j+1]): 		#int() for ValueError exception
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr


def simple_assert_test():
	assert list(BubbleSort([])) == []
	assert list(BubbleSort([1,3,2])) == [1,2,3], BubbleSort([1,3,2])
	assert list(BubbleSort([2,-3,1])) == [-3,1,2], BubbleSort([2,-3,1])
	print("OK")



class TestBubbleSort(unittest.TestCase):
	def setUp(self):
		print("SetUp")

	def test_empty(self):
		self.assertTrue(BubbleSort([]) == [])

	def test_arr(self):
		self.assertEqual(BubbleSort([2, 1, 3]), [1, 2, 3])

	def test_arr_negative(self):
		self.assertEqual(BubbleSort([2,-1,-3]), [-3, -1, 2])

	def test_arr_exception(self):
		with self.assertRaises(ValueError):
			BubbleSort([1,3,"2a"])

	def tearDown(self):
		print("tearDown")



if __name__ == '__main__':
	simple_assert_test()
	doctest.testmod()
						#or python3 -m doctest test.py 

	unittest.main() 	
						#or python3 -m unittest test.py (-v = full log)
						#or python3 -m unittest test.TestBubbleSort
						#or python3 -m unittest test.TestBubbleSort.test_empty



	
