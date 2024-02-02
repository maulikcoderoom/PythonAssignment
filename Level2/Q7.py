number_list = [7, 2, 5, 1, 9, 3]
sorted_list = sorted(number_list)
length = len(sorted_list)
if length % 2 != 0:
    median = sorted_list[length // 2]
else:
    middle_right = sorted_list[length // 2]
    middle_left = sorted_list[length // 2 - 1]
    median = (middle_right + middle_left) / 2

print("median is ",median)