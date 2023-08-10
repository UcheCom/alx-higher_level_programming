#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
n = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - n)), end="")
    n = 32 if n == 0 else 0
