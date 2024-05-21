def is_eligible(N):
    # Check if the number of people falls within the range of 6 to 8 inclusive
    if 6 <= N <= 8:
        return "Yes"
    else:
        return "No"

# Main function to handle input/output
def main():
    # Input the number of people 
    N = int(input().strip())

    # Check eligibility and print the result
    print(is_eligible(N))

# Run the main function
if __name__ == "__main__":
    main()