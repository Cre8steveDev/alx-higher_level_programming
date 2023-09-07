#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    usage_string = "Usage: {} <a> <operator> <b>".format(argv[0])
    operators_str = ['+', '-', '*', '/']

    if len(argv) != 4:
        print(usage_string)
        exit(1)

    if argv[2] not in operators_str:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = 0
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        result = add(a, b)

    elif argv[2] == "-":
        result = sub(a, b)

    elif argv[2] == "*":
        result = mul(a, b)

    elif argv[2] == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(a, argv[2], b, result))
