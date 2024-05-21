def is_good_turn(X, Y):
    total = X + Y
 
    if total > 6:
        return "YES"
    else:
        return "NO"

def main():
    # Input the number of test cases
    T = int(input().strip())

    for _ in range(T):
        
        X, Y = map(int, input().strip().split())

        print(is_good_turn(X, Y))

# Run the main function
if __name__ == "__main__":
    main()