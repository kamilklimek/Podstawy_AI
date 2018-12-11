import unittest
import MatrixOperations as MO

class TestMatrixOperations(unittest.TestCase):

    def test_matrix_add(self):
        #given
        a = [
            [1, 2, 3],
            [4, 1, 2]
        ]

        b = [
            [1, 3, 1],
            [4, 6, 6]
        ]

        expected = [
            [2, 5, 4],
            [8, 7, 8]
        ]
        
        #when
        result = MO.add_matrix(a, b)

        #expected
        self.assertEqual(expected, result)

    def test_matrix_substraction(self):
        #given
        a = [
            [1, 2, 3],
            [4, 1, 2]
        ]

        b = [
            [1, 3, 1],
            [4, 6, 6]
        ]

        expected = [
            [0, -1, 2],
            [0, -5, -4]
        ]
        
        #when
        result = MO.substract(a, b)

        #expected
        self.assertEqual(expected, result)

    def test_matrix_multiply_1(self):
        #given
        a = [
            [1, 2, 3],
            [4, 1, 2]
        ]

        b = [
            [1, 3],
            [4, 6],
            [2, 4]  
        ]

        expected = [
            [15, 27],
            [12, 26]
        ]

        #when
        result = MO.multiply(a, b)

        #expected
        self.assertEqual(expected, result)

    def test_matrix_multiply_2(self):
        #given
        a = [
            [1, 2],
            [4, 1]
        ]

        b = [
            [1, 3],
            [4, 6]  
        ]

        expected = [
            [9, 15],
            [8, 18]
        ]

        #when
        result = MO.multiply(a, b)

        #expected
        self.assertEqual(expected, result)

    
if __name__ == '__main__':
    unittest.main()