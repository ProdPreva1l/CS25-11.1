import unittest
from unittest.mock import patch, call

from main import character_select
from utils.utils import menu, speak


class TestUtils(unittest.TestCase):
    @patch('builtins.input', return_value='2')
    def test_character_select(self, _):
        expected = "Roxy"
        actual = character_select()
        self.assertEqual(expected, actual.name)

    @patch('builtins.input', return_value='3')
    def test_menu(self, _):
        expected = "NO!"
        actual = menu("Are you stupid?", "Yes", "Obviously!", "NO!")
        self.assertEqual(expected, actual[1])

    @patch('builtins.print')
    @patch('time.sleep', return_value=None)
    def test_typewriter(self, _, mock):
        text = "hello there little friend!"
        speak(text)

        expected_calls = [call(char, end='', flush=True) for char in text]
        mock.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(mock.call_count, len(text))

if __name__ == '__main__':
    unittest.main()
