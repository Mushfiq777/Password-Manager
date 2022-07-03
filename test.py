import os


import os
from turtle import window_width
a = "hello world"
b = "helllllll"
width = os.get_terminal_size().columns
print(a.center(width).rstrip().rjust(25,"#"))
print(b.center(width))
print(a.ljust(-2,"%"))
print(b.rjust(23,"%"))