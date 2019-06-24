import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
   
   def test_get_cages0(self):
      cages = [[5, 2, 0, 5],
               [3, 1, 1],
               [8, 3, 2, 3, 4]]
      self.assertEqual(cages, get_cages())
      
   def test_check_rows0(self): 
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle))

   def test_check_rows1(self):
       puzzle = []
       puzzle.append([1,5,3,4,2])
       puzzle.append([2,3,4,1,5])
       puzzle.append([3,4,1,5,2])
       puzzle.append([4,2,5,3,1])
       puzzle.append([3,4,1,5,2])
       self.assertTrue(check_rows_valid(puzzle))

   def test_check_rows2(self):
       puzzle = []
       puzzle.append([1,5,3,4,2])
       puzzle.append([2,3,4,1,5])
       puzzle.append([3,4,1,5,2])
       puzzle.append([4,2,5,3,1])
       puzzle.append([3,3,1,5,2])
       self.assertFalse(check_rows_valid(puzzle))

   def test_check_rows3(self):
       puzzle = []
       puzzle.append([1,5,3,4,2])
       puzzle.append([2,3,4,1,5])
       puzzle.append([3,4,1,5,2])
       puzzle.append([4,2,5,3,1])
       puzzle.append([3,1,1,5,2])
       self.assertFalse(check_rows_valid(puzzle))
      
   def test_check_columns0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_columns_valid(puzzle))

   def test_check_columns1(self):
       puzzle = []
       puzzle.append([5, 1, 2, 3, 4])
       puzzle.append([1, 2, 3, 4, 5])
       puzzle.append([2, 3, 4, 5, 1])
       puzzle.append([3, 4, 5, 1, 2])
       puzzle.append([4, 5, 1, 2, 3])
       self.assertTrue(check_columns_valid(puzzle))

   def test_check_columns2(self):
       puzzle = []
       puzzle.append([5, 1, 2, 3, 4])
       puzzle.append([1, 2, 3, 4, 5])
       puzzle.append([3, 4, 4, 5, 1])
       puzzle.append([4, 3, 5, 1, 2])
       puzzle.append([4, 5, 1, 2, 3])
       self.assertFalse(check_columns_valid(puzzle))

   def test_check_cages0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_cages_valid(puzzle, cages))

   def test_check_cages1(self):
      puzzle = []
      puzzle.append([5, 3, 1, 4, 2])
      puzzle.append([3, 2, 4, 5, 1])
      puzzle.append([2, 1, 5, 3, 4])
      puzzle.append([1, 4, 3, 2, 5])
      puzzle.append([4, 5, 2, 1, 3])
      cages = []
      cages.append([10, 3, 0, 5, 6])
      cages.append([4, 2, 1, 2])
      cages.append([7, 3, 3, 4, 9])
      cages.append([3, 2, 10, 11])
      cages.append([9, 2, 7, 12])
      cages.append([8, 2, 8, 13])
      cages.append([9, 2, 14, 19])
      cages.append([10, 3, 15, 20, 21])
      cages.append([9, 3, 16, 17, 22])
      cages.append([2, 1, 18])
      cages.append([4, 2, 23, 24])
      self.assertTrue(check_cages_valid(puzzle, cages))

if __name__ == '__main__':
   unittest.main()
