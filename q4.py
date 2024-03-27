# Write a Python function printStats(t) which retrives data in a text file t which reads in lines of numbers. For each line read in, 
# the function must call a decorator function which prints

# Decorator functionv prints
# The numbers read
# The count of the numbers read
# The average of the numbers
# The maximum of the numbers
def decorator(func):
    def wrapper(numbers):
        numNumbers = len(numbers)
        total = sum(numbers)
        average = total / numNumbers if numNumbers > 0 else 0
        maximum = max(numbers) if numNumbers > 0 else None
        print("The numbers read:", numbers)
        print("The count of the numbers read:", numNumbers)
        print("The average of the numbers:", average)
        print("The maximum of the numbers:", maximum)
        # Argument given to the function identify_decorator()
        # call the function assigned to the variable func
        func(numbers) 
    return wrapper

# Function printState()
@decorator
def process_numbers(numbers):
    pass

def printStats(t):
    file = open("numbers.txt", "r")
    for line in file:
        numbers = [int(num) for num in line.split()]
        process_numbers(numbers) #skip the line

printStats("numbers.txt")

