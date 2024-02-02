def sum_of_odd_numbers(start, stop):
    odd_sum = 0
    for num in range(start, stop + 1):
        if num % 2 != 0:
            odd_sum += num
    return odd_sum

start = 1
stop = 10

odd_sum = sum_of_odd_numbers(start, stop)
print("Sum of odd numbers:", odd_sum)
