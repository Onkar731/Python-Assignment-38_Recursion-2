"""
Write a recursive function to print cubes of first N natural numbers
"""

# defining a function "print_cubes()" which takes a number as an argument
# and print cubes of first N natural number
def print_cubes(num):
    if num >= 1:
        print_cubes(num-1)
        print(num**3, end=' ')
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_cubes()
print_cubes(N)