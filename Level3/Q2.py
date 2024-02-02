def count_lines(file_name):
    line_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

file_name = 'Testdata/doc1.txt'
num_lines = count_lines(file_name)
print("Number of lines in", file_name, ":", num_lines)
