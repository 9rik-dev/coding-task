#!/usr/bin/env python3

from unittest import TestCase, main
from unittest import main as run_test
import main

 
CONV_TEST = [
    ("+0", 0),  # rip two's complement
    ("12345", 12345),
    ("-12335", -12335), 
    ("+13", 13),
    ("0645", 645),
    ("-00998", -998),
    ("043009", 43009),
    # interpreter handles 'longs' internally
    ("950234295879239129094870938129805981790847901238749081230749",
        950234295879239129094870938129805981790847901238749081230749)
]

ERR_TEST = [
    ("", ValueError),  # undefined
    ("0", ValueError),  # 2 <= |s| constraints p.2
    ("+", ValueError),
    ("o53V", TypeError),  # conversion error
    ("-99+32", TypeError),  # wrong sign placement
    ("--011", TypeError),
]


class NumberFormatterTestCase(TestCase):

    def test_parseInt(self):
        t = main.NumberFormatter().parseInt
        print("\n")
        for inp, exp in CONV_TEST:
            print(f"RUNNING: parseInt('{inp}') -> {exp}")
            with self.subTest():
                self.assertEqual(t(inp), exp)
        for inp, exp in ERR_TEST:
            print(f"RUNNING: parseInt('{inp}') -> {exp.__name__}")
            with self.subTest():
                self.assertRaises(exp, t, inp)


if __name__ == "__main__":
    run_test(verbosity=2)
