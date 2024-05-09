# Function to determine the correctness of the guess word
def correctness(S, T):
    M = ""
    for i in range(len(S)):
        if S[i] == T[i]:
            M += "G"  # If guess is correct, add 'G' to M
        else:
            M += "B"  # If guess is wrong, add 'B' to M
    return M


