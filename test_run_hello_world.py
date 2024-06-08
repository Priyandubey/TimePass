import unittest

from run_hello_world import run_hello_word_echo

import heapq

class TestHelloWorld(unittest.TestCase):

    def test_run_hello_word_echo(self):
        s = "Hi_"
        expected = ["H", "i", "_"]

        pq = list(expected)
        heapq.heapify(pq)
        print(pq)

        self.assertEqual(run_hello_word_echo(s), expected)

if __name__ == '__main__':
    unittest.main()