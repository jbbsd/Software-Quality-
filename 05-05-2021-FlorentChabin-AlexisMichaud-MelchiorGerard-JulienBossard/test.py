import unittest
import sort


class TestAppFile(unittest.TestCase):
    def test_readFile(self):
        self.assertFalse(sort.readFile('numbers.json'))
        self.assertFalse(sort.readFile('numbers.docx'))
        self.assertFalse(sort.readFile('numbs.txt'))
        self.assertFalse(sort.readFile('numbers.txt'))
        self.assertFalse(sort.readFile('omer.txt'))

    def test_parseLine(self):
        self.assertEqual(sort.parseLine('5 -45 toto 23 1'), [5, -45, 23, 1])


if __name__ == "__main__":
    unittest.main()
