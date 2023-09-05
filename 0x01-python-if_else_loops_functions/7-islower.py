#!/usr/bin/python3
def islower(c):
    mode = ord(c)
    if mode > 96 and mode < 123:
        return True
    else:
        return False
