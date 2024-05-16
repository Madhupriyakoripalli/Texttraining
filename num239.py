T = int(input())

for _ in range(T):
    L, R = map(int, input().split())
    count = 0
    for num in range(L, R + 1):
        if num % 10 == 2 or num % 10 == 3 or num % 10 == 9:
            count += 1
    print(count)
