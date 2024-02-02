def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum = i + divisor_sum
    
    return divisor_sum == number

number = int(input("input: "))

if is_perfect_number(number):
    print("output:", "Yes")
else:
    print("output:", "No")
