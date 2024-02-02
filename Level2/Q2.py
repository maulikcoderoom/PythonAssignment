list1 = [1, 2, 2, 3, 4, 4, 5, 5]
outlist=[]
for item in list1:
    if item not in outlist:
        outlist.append(item)

# Print the output list
print("Sample Output:", outlist)