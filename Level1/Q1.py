def print_msg(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Consultadd - Python Training")
    elif number % 3 == 0:
        print("Consultadd")
    elif number % 5 == 0:
        print("Python Training")
    else:
        print("Number is not divisible by 3 or 5")

# Test the function with some numbers
numbers = [5, 3, 15, 7]
for num in numbers:
    print_msg(num)