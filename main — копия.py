with open("test.txt", "r") as myfile:
  myfile.read()
with open("test2.txt", "r") as myfile:
    myfile.read()

import ast
my_tree = ast.parse("a")
print(ast.dump(my_tree))

import ast
my_tree = ast.parse("w")
print(ast.dump(my_tree))

import textdistance
textdistance.hamming("test2.txt", "test.txt")