
"""O(n) complexity algo"""
colors = ["green", "yellow", "blue", "pink"]    # n = 4
def linear(colors):
    for color in colors:
        print(color)

linear(colors)  # n = 4 operations
print("This is a linear time algorithmm")

"""O(n^2) complexity algo"""
colors = ["green", "yellow", "blue", "pink"]    # n = 4
def quadratic(colors):
    for first in colors:
        for second in colors:
            print(first, second)
            for third in colors:
                print(first, second, third)

quadratic(colors)
print("This is a quadratic time algorithm")

"""O(n^3) complexity algo"""
colors = ["green", "yellow", "blue", "pink"]    # n = 4
def cubic(colors):
    for first in colors:
        for second in colors:
            print(first, second)
            for third in colors:
                print(first, second, third)

cubic(colors)
print("This is a cubic time algorithm")

"""Calculating Big O Notation"""
colors = ["green", "yellow", "blue", "pink", "black", "white", "purple"]    # O(1)
other_colors = ["orange", "brown"]  # O(1)

# Complex Algorithm
def complex_algotithm(colors):
    color_count = 0     # O(1)

    for color in colors:
        print(color)    # O(n)
        color_count += 1   # O(n)

    for other_color in other_colors:
        print(other_color)  # O(m)
        color_count += 1 # O(m)
    
    print(color_count)  # o(1)

complex_algotithm(colors) 

#   1. Remove constants
#   2. Differnt variables for differnt input
#   3. Remove smaller term
#
 
