#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    argv = sys.argv
    operators = "+-*/"
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (argv[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if (argv[2] == '+'):
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif (argv[2] == '-'):
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif (arg[2] == '*'):
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
