# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of songs in the playlist
    n = int(input())
    
    # Read the lengths of Vlad's songs
    lengths = list(map(int, input().split()))
    
    # Read the position of "Uncle Johny" in the initial playlist
    k = int(input())
    
    # Find the length of the song "Uncle Johny"
    uncle_johny_length = lengths[k - 1]
    
    # Sort the playlist
    sorted_lengths = sorted(lengths)
    
    # Find the position of "Uncle Johny" in the sorted playlist
    for i in range(n):
        if sorted_lengths[i] == uncle_johny_length:
            print(i + 1)
            break
