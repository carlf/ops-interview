#!/usr/bin/env python

# This kills the machine. How do I make it work?
# print sum(range(1000000000))

def generate_evens(n):
    numbers = []
    x = 2
    while x < n:
        numbers.append(x)
        x += 2
    return numbers

for i in generate_evens(100):
    print i

# Why would this not work? How would we fix it?
# for i in generate_evens(1000000000):
#    print i
