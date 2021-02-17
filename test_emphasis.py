from unittest import TestCase
from emphasis import eprint
import unittest


class TestEmphasis(TestCase):
    def test_eprint(self):
        eprint("this is really bad`danger` and I dont know`info` what to do")
        self.assertEqual("a", "a")


if __name__ == "__main__":
    unittest.main()