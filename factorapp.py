"""
Factor Generator App
Finds all factors of a user-input number and displays factor pairs.
"""

print("Welcome to my Factor Generator App!")  # Welcome message

active = True  # Main loop control flag

while active:
    input_number = int(input("Enter a number to find its factors: "))
    factors = []
    # Collect all factors of input_number
    for i in range(1, input_number + 1):
        if input_number % i == 0:
            factors.append(i)
    # Print all factors
    print(f"The factors of {input_number} are:")
    for factor in factors:
        print(factor)
    print()
    # Print unique factor pairs
    print("Summary of factor pairs:")
    for i in range(int(len(factors) / 2)):
        factor1 = factors[i]
        factor2 = factors[-(i + 1)]
        print(f"{factor1} * {factor2} = {input_number}")
    # Print middle factor squared if odd number of factors
    if len(factors) % 2 == 1:
        middle = factors[len(factors) // 2]
        print(f"{middle} * {middle} = {input_number}")
    print()
    # Ask to run again or exit
    user_response = input("Do you want to find factors for another number? (yes/no): ").strip().lower()
    if user_response != "yes":
        active = False
        print("Thank you for using my Factor Generator App!")


# ==========================================
# PROGRAM STRUCTURE NOTES
# ==========================================
"""
Key Python concepts:
- While loops with flag control
- For loops with range()
- List operations (append, indexing)
- Modulo operator (%) for divisibility
- String formatting for output
- User input handling

Factor pairing logic:
- factors[0] pairs with factors[-1] (first with last)
- factors[1] pairs with factors[-2] (second with second-to-last)
- factors[i] pairs with factors[-(i+1)] (general pattern)
- Only need to loop through first half of list
"""

