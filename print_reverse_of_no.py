"""
Write a recursive function to print reverse of a given number
"""

# defining a function "print_reverse()" which takes a number as an argument
# and prints the reverse of that number
def print_reverse(num):
    if num != 0:
        print(num%10, end='')
        print_reverse(num//10)
        
    
# taking input from the user
num = int(input("Enter a number : "))

# calling print_reverse()
print_reverse(num)