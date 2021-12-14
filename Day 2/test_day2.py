import unittest
import day2

sampleFile = open("sample.txt")
sampleData = sampleFile.readlines()
sampleFile.close()

class TestDay(unittest.TestCase):
    def test_partOne(self):
        position = day2.partOne(0, sampleData)
        self.assertEqual(position, 150)

    def test_partTwo(self):
        position = day2.partTwo(0, sampleData)
        self.assertEqual(position, 900)


if __name__ == '__main__':
    unittest.main()
