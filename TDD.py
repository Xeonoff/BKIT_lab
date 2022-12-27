import unittest
import sys, os

sys.path.append(os.getcwd()) #current working directory
from main import *

#==============================================================================================================

class TestGenRandom(unittest.TestCase):
    def test_gen_random_returns_list(self):
        self.assertEqual(list(set(gen_random(100,1,3))),[1,2,3])
        self.assertEqual(list(set(gen_random(0, 4, 6))), [])

    def test_gen_random_receives_not_integer_returns_empty(self):
        self.assertEqual(gen_random(1.1, 2, 3), [])
        self.assertEqual(gen_random(1, 12.3, 4), [])
        self.assertEqual(gen_random(15, 2, 14.11), [])

    def test_gen_random_receives_alpha_string_returns_empty(self):
        self.assertEqual(gen_random('a', 2, 3), [])
        self.assertEqual(gen_random(1, 'a', 4), [])
        self.assertEqual(gen_random(15, 2, 'a'), [])

#==============================================================================================================

class TestCmTimer(unittest.TestCase):
    def test_cm_timer_returns_same(self):
        self.assertEqual(3, 3)
        self.assertEqual(4, 4)
        self.assertEqual(5, 5)

    def test_cm_timer_returns_integer(self):
        self.assertIsInstance(cm_timer(3),int)

    def test_cm_timer_receives_string_returns_integer(self):
        self.assertEqual(cm_timer('2'),2)

    def test_cm_timer_receives_alpha_string_returns_zero(self):
        self.assertEqual(cm_timer('asdadassda'),0)

#==============================================================================================================

class TestSort(unittest.TestCase):
    def test_sort_returns_sorted_list(self):
        self.assertEqual(sort([4, -30, 100, -100, 123, 1, 0, -1, -4]),[123, 100, -100, -30, 4, -4, 1, -1, 0])

    def test_sort_receives_not_list(self):
        self.assertEqual(sort(1),0)
        self.assertEqual(sort(1.11), 0)
        self.assertEqual(sort('a'), 0)

if __name__=='__main__':
    unittest.main()