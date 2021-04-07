import unittest
from main import leng


class test_done(unittest.TestCase):

    def test_length(self):

        a=leng([1,2,3,4,5])
        self.assertEqual(a,5)

if __name__ == '__main__':
    unittest.main()
