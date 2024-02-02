my_list = [1, 2, 3, 4, 5]
try:
    result = my_list[5]
    print("Result of the operation:", result)
except IndexError:
    print("Index is out of range.")