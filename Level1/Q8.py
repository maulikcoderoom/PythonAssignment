def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

number1 = 12
number2 = 18

lcm_value = lcm(number1, number2)

print(f"LCM of {number1} and {number2} is: {lcm_value}")