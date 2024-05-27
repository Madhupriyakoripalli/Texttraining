# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of animals in the store
    n = int(input())
    
    # Read the types of animals
    animals = list(map(int, input().split()))
    
    # Count the frequency of each animal type
    animal_count = {}
    for animal in animals:
        if animal in animal_count:
            animal_count[animal] += 1
        else:
            animal_count[animal] = 1
    
    # Check if it's possible for Alice and Bob to have the same multiset of animals
    possible = True
    for count in animal_count.values():
        if count % 2 != 0:
            possible = False
            break
    
    # Print the result
    if possible:
        print("YES")
    else:
        print("NO")
