def get_count_digits_letters(input_string):
    num_digits = 0
    num_letters = 0

    for char in input_string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1

    return num_letters, num_digits

input_string = input("Enter a string: ")
num_letters, num_digits = get_count_digits_letters(input_string)
print(f"Given input string {input_string} has Alphabets: {num_letters} & Numbers: {num_digits}")