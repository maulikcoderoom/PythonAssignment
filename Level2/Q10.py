def stone_piles(n):
    piles = []
    start = 2 if n % 2 == 0 else 1
    
    for i in range(n):
        piles.append(start)
        start += 2
        
    return piles

n = int(input("Enter the number of stone piles: "))
stones_per_pile = stone_piles(n)
print("Number of stones in each pile:", stones_per_pile)