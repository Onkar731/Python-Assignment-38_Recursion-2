"""
Write a recursive function to print squares of first N natural numbers
"""

# defining a function "print_squares()" which takes a number as an argument
# and print squares of first N natural number
def print_squares(num):
    if num >= 1:
        print_squares(num-1)
        print(num**2, end=' ')
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_squares()
print_squares(N)