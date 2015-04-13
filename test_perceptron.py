from mock import call, patch
import unittest

from perceptron import Perceptron


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

    def test_get_weights_returns_weights_stored_in_perceptron(self):
        self.perceptron.weights = [0.5, 0.5, 0.5]

        expected = [0.5, 0.5, 0.5]
        actual = self.perceptron.get_weights()

        self.assertEqual(actual, expected)

    @patch('perceptron.random.uniform')
    def test_give_weights_random_value_when_create_perceptron(
        self,
        mock_uniform
    ):
        expected = [0.1, 0.2, 0.3]
        mock_uniform.side_effect = expected

        perceptron = Perceptron()

        actual = perceptron.get_weights()

        self.assertEqual(actual, expected)

        self.assertEqual(mock_uniform.call_count, 3)

        expected_calls = [
            call(-1, 1),
            call(-1, 1),
            call(-1, 1)
        ]
        self.assertEqual(mock_uniform.mock_calls, expected_calls)


if __name__ == '__main__':
    unittest.main()
