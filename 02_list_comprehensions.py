#!/usr/bin/env python

a0 = [0, 1, 2, 3, 4, 5]
a1 = [x**2 for x in a0]
a2 = [2**x for x in a0]
a3 = [2 * x for x in range(10) if x % 2 == 1]

assert a0 == False
assert a1 == False
assert a2 == False
assert a3 == False
