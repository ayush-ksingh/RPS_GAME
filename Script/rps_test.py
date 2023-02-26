from contextlib import redirect_stdout
from unittest.mock import patch
import rps_game as rps
import unittest
import io


class TestRockPaperScissors(unittest.TestCase):
    def test_check_stats(self):
        rps.check_stats(0)
        self.assertEqual(rps.win, 1)
        rps.check_stats(1)
        self.assertEqual(rps.lose, 1)
        rps.check_stats(2)
        self.assertEqual(rps.tie, 1)

    def test_check_win(self):
        self.assertEqual(rps.check_win(0, 1), "lose!")
        self.assertEqual(rps.check_win(0, 2), "win!")
        self.assertEqual(rps.check_win(0, 0), "tied!")

        self.assertEqual(rps.check_win(1, 0), "win!")
        self.assertEqual(rps.check_win(1, 2), "lose!")
        self.assertEqual(rps.check_win(1, 1), "tied!")

        self.assertEqual(rps.check_win(2, 0), "lose!")
        self.assertEqual(rps.check_win(2, 1), "win!")
        self.assertEqual(rps.check_win(2, 2), "tied!")

        with self.assertRaises(ValueError):
            rps.check_win(3, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[0, 5])
    def test_game(self, mock_input, mock_output):
        rps.game()
        self.assertIn("Thanks for Playing!", mock_output.getvalue())

    def test_display_stats(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            rps.display_stats(2, 3, 4, "test")
            output = buf.getvalue().strip()
            print(output)
            expected_output = "You won 2 times!\n\nYou lost 3 times!\n\nYou tied 4 times!\n\nYou have a 22.22% win " \
                              "rate on test!"
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
