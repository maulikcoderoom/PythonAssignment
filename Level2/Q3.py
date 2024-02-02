def count_pairs_with_sum(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    pair_count = 0

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            pair_count += 1
            left += 1
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    
    return pair_count

# Sample input
arr = [1, 2, 3, 4, 5]
k = 6

pair_count = count_pairs_with_sum(arr, k)
print("Sample Output:", pair_count)