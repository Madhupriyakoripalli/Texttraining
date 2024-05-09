# Function to determine the correctness of the guess word
def correctness(S, T):
    M = ""
    for i in range(len(S)):
        if S[i] == T[i]:
            M += "G"  # If guess is correct, add 'G' to M
        else:
            M += "B"  # If guess is wrong, add 'B' to M
    return M

# Input the no of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Input the hidden word and guess word
    S = input().strip()
    T = input().strip()
    
    # Determine correctness of the guess word
    M = correctness(S, T)
    
    # Output the result
    print(M)
