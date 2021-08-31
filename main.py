#!/usr/bin/env python3

"""Utility module for parsing and converting types"""

class NumberFormatter:
    """Convert numeric values represented by various
    types into type <int>

    Attr
    ----
    N : class attribute, mapping of digits [str]int

    Methods
    -------
    parseInt(to_int: str) -> int:
        convert string with numeric data into <int>
    """

    N = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    }

    def parseInt(self, to_int: str) -> int:
        """Convert string of digits into <int>:
        '98' -> 98, '-12345' -> -12345, '+1' -> 1
        Strings with leading zeros are valid inputs
        Decimal values are not supported

        Args
        ----
        to_int : <str>
            string to convert into <int> value

        Raise
        -----
        ValueError : on insufficient string length
        TypeError : on invalid char or misplaced sign

        Return
        ------
        int : integer value of 'to_int' string
        """

        # IDK what you meant by applicable p.1
        if len(to_int) == 0:
            raise ValueError("Cannot convert an empty string")
        # 2 <= |s| p.2
        if len(to_int) == 1:
            raise ValueError("Insufficient string length")

        # handle sign if present
        if to_int[0] == "+":
            sign, to_int = 1, to_int[1:]
        elif to_int[0] == "-":
            sign, to_int = -1, to_int[1:]
        else: sign = 1

        # so just in case p.3-4
        for char in to_int:  # check invalid chars
            try: self.N[char]
            except KeyError:
                # in case someone puts sign in the middle of the string
                if char in "+-":
                    warn = f"Wrong placement '{char}' sing"
                    # original exception available in __context__
                    raise TypeError(warn) from None
                warn = f"Cannot convert '{char}' to digit"
                raise TypeError(warn) from None

        # construct <int> from 'to_int' digits
        res, dec = 0, len(to_int) - 1
        for i, char in enumerate(to_int):
            res += self.N[char] * 10 ** (dec - i)

        return res * sign
