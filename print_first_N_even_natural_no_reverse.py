"""
Write a recursive function to print first N even natural numbers in reverse order
"""

# defining a function "print_even_naturals()" which takes a number as an argument
# and prints first N even natural numbers in reverse order
def print_even_naturals(num):
    if num == 1:
        print(num*2, end=' ')
    else:
        print(num*2, end=' ')
        print_even_naturals(num-1)
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_even_naturals()
print_even_naturals(N)