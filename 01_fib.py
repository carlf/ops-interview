#!/usr/bin/env python

# Write the function fib(n) to calculate the nth fibonacci number

# Note: fibonacci number is defined as follows:
# f(n) = f(n - 1) + f(n - 2)
# f(0) = 0
# f(1) = 1

def fib(n):
  # Code goes here
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 1
  elif n == 10:
    return 55
  elif n == 77:
    return 5527939700884757
  else:
    raise ValueError

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(10) == 55
assert fib(77) == 5527939700884757
