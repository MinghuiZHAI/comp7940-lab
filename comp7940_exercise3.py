# Write a program to find all factors of the numbers in the list l

def print_factor(x):
    # your code here
    # x = 52633
    for i in range(2, x):
        # your code here
        if x % i == 0: 
            print(i)
    print(1)
    print(x)  

l = [52633, 8137, 1024, 999]

# your code here
for number in l:
    print(f"Factors of {number}:")
    print_factor(number)
    print("-----")