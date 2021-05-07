import unittest


def addtwonumbers(a,b):
    return a+b


class AddTest(unittest.TestCase):
    def test1(self):
        c= addtwonumbers(5,6)
        self.assertEqual(c,11)

    def test2(self):
        c= addtwonumbers(5,10)
        self.assertNotEqual(c,10)


if __name__ == '__main__':
    unittest.main()
