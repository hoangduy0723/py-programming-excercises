"""Noonerize Me
https://www.codewars.com/kata/noonerize-me

Spoonerize... with numbers... numberize?... numboonerize?... noonerize? ...anyway!  If you don't yet know what a spoonerism is and haven't yet tried my spoonerism kata, please do [check it out](http://www.codewars.com/kata/spoonerize-me) first.

You will create a function which takes an array of two positive integers, spoonerizes them, and returns the positive difference between them as a single number or ```0``` if the numbers are equal:
```
[123, 456] = 423 - 156 = 267
```
Your code must test that all array items are numbers and return ```"invalid array"``` if it finds that either item is not a number.  The provided array will always contain 2 elements.

When the inputs are valid, they will always be integers, no floats will be passed.  However, you must take into account that the numbers will be of varying magnitude, between and within test cases.
"""


def noonerize(numbers):
    def spoonerize(numbers):
        a, b = [str(n) for n in numbers]
        return "{}{} {}{}".format(b[0], a[1:], a[0], b[1:])

    if all(isinstance(n, int) for n in numbers):
        numbers = spoonerize(numbers).split()
        a, b = map(int, numbers)
        return abs(a - b)
    else:
        return "invalid array"
