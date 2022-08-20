import unittest
import app


class AppTests(unittest.TestCase):
    def test_main_output(self):
        output = app.main()
        self.assertEqual(output, 'stub')


if __name__ == '__main__':
    unittest.main()
