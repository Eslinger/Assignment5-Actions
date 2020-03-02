import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circle(self):
        expected = 50.26548245743669
        self.assertEqual(expected, task.circle(4))

    def test_first_last(self):
        myList = ["This", "is", "a", "test"]
        expected = ["This", "test"]
        self.assertEqual(expected, task.first_last(myList))

    def test_date_days(self):
        date1 = datetime.datetime(2019, 9, 15)
        date2 = datetime.datetime(2020, 9, 15)
        expected = 366
        self.assertEqual(expected, task.date_days(date1, date2))


if __name__ == '__main__':
    unittest.main()
