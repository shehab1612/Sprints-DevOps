import sprints
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sprints.MyFunc([1,2,3,4,5,6,1.1,1.2,1.3]), (4, 1.3), "Should be (4, 1.3)")
        
    def test_sum2(self):
        self.assertEqual(sprints.MyFunc([1.1,1.2,1.3]), ('there are no even integers', 1.3), "Should be ('there are no even integers', 1.3)")
        
    def test_sum3(self):
        self.assertEqual(sprints.MyFunc([1,2,3,4,5,6,7,8]), (5, 'there are no floats'), "Should be (5, 'there are no floats')")
        
    def test_sum4(self):
        self.assertEqual(sprints.MyFunc([0,0,0,0,0]), (0, 'there are no floats'), "Should be (0, 'there are no floats')")
        
    def test_sum5(self):
        self.assertEqual(sprints.MyFunc(["shehab","mohamed","khalil"]), (0), "Should be (0)")
        
if __name__ == '__main__':
    unittest.main()