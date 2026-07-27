# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    total= 0.0
    for num in numbers:
     total += num
    return total
def calculate_average(numbers):
    if not numbers:
        return 0
    total_sum = calculate_sum(numbers)
    return total_sum/ len(numbers)
def calculate_maximum(numbers):
    current_max=numbers[0]
    for num in numbers: 
        if num > current_max:
            current_max = num
    return current_max
        
def calculate_minimum(numbers):
    current_min=numbers[0]
    for num in numbers: 
        if num < current_min:
            current_min = num
    return current_min
if __name__== "__main__":
  n = int(input("how many numbers?"))
  if n<=0:
    print("Error: The number of items must be a positive integer.")
  else:
    user_numbers =[]
    for i in range(n):
     val = float(input(f"Enter number {i+1}"))
     user_numbers.append(val)
    print("\nResults:")
    
    total = calculate_sum(user_numbers)
    maximum = calculate_maximum(user_numbers)
    minimum= calculate_minimum(user_numbers)

    print(f"Sum: {int(total) if total.is_integer() else total}")
    print(f"Average: {calculate_average(user_numbers)}")
    print(f"Maximum: {int(maximum) if maximum.is_integer() else maximum}")
    print(f"Minimum: {int(minimum) if minimum.is_integer() else minimum}")
