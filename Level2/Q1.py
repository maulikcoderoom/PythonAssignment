l1 = [1, 2, 4, 4, 5]
l2 = [4, 5, 6, 7, 8]
ce=[]
for item in l1:
    if item in l2 and item not in ce:
        ce.append(item)
print("Sample Output:", ce)