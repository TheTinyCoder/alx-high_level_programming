#!/usr/bin/python3
import sys
sys.path.append('../')
Square = __import__('6-square').Square

try:
    my_square = Square(3, "Position")
except Exception as e:
    print(e)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
