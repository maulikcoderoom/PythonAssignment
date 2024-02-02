string = "Hello, World!"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1

print("Sample Output:", vowel_count)