arr = [1, 2, 3, 4, 5]
D = 2

rotate_index = len(arr) - D
rotated_arr = arr[rotate_index:] + arr[:rotate_index]
rotated_arr
print("Sample Output:", rotated_arr)