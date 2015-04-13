from perceptron import Perceptron
import unittest


class PerceptronTest(unittest.TestCase):
    def setUp(self):
        self.perceptron = Perceptron()

    def test_activate_func_returns_positive_one_if_input_is_greater_than_zero(
        self
    ):
        expected = 1
        actual = self.perceptron.activate(5)

        self.assertEqual(actual, expected)

    def test_activate_func_returns_negative_one_if_input_is_less_than_zero(
        self
    ):
        expected = -1
        actual = self.perceptron.activate(-10)

        self.assertEqual(actual, expected)

    def test_activate_func_returns_negative_one_if_input_is__zero(self):
        expected = -1
        actual = self.perceptron.activate(0)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
