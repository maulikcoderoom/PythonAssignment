def sum_of_digits(num):
    sum_digits = sum(int(digit) for digit in str(num))
    if sum_digits < 10:
        return sum_digits
    else:
        return sum_of_digits(sum_digits)
num = 987

output_sum = sum(int(digit) for digit in str(num))

print("Sample Output:", output_sum)
final_output = sum_of_digits(output_sum)
print("Final Output:", final_output)