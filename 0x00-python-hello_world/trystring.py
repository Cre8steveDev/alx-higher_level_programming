import sys

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
arr = str.split(" ")

newlist = (arr[5], arr[6],  arr[12], arr[0])

newStr = " ".join(newlist)
print(newStr)

sys.stderr.write("Error Message")
sys.exit(1)
