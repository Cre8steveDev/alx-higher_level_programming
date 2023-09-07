#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1
    arg_string = "argument" if arg_len == 1 else "arguments"
    str_delim = "." if arg_len == 0 else ":"

    print("{} {}{}".format(arg_len, arg_string, str_delim))

    for i in range(1, arg_len + 1):
        print("{}: {}".format(i, argv[i]))
