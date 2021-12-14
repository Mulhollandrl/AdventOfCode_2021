import unittest
import day1

sampleFile = open("sample.txt")
sampleData = sampleFile.readlines()
sampleFile.close()

class TestDay(unittest.TestCase):
    def test_partOne(self):
        totalIncreases = day1.partOne(0, sampleData)
        self.assertEqual(totalIncreases, 7)

    def test_partTwo(self):
        totalIncreases = day1.partTwo(0, sampleData)
        self.assertEqual(totalIncreases, 5)


if __name__ == '__main__':
    unittest.main()
