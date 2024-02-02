def read_even_length_strings(file_name):
    even_length_strings = []
    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if len(word) % 2 == 0:
                    even_length_strings.append(word)
    return even_length_strings

file_name = 'Testdata/doc1.txt'
even_length_strings = read_even_length_strings(file_name)
for string in even_length_strings:
    print(string)