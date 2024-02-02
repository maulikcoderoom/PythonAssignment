def is_power_of_two(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n < 1:
        return False
    else:
        return is_power_of_two(n // 2)
n=6        
print(is_power_of_two(n))