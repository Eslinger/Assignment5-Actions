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


if __name__ == '__main__':
    unittest.main()
