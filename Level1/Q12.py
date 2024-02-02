def reverse_number(num):
    revnum = 0
    while num > 0:
        digit = num % 10     
        revnum = revnum * 10 + digit   
        num = num // 10     
    return revnum

num = 12345

revnum = reverse_number(num)
print("Sample Output:", revnum)