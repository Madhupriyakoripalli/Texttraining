# Input the number of integers in the list
N = int(input())


integer_list = []
for _ in range(N):
    integer_list.append(int(input()))


sorted_list = sorted(integer_list)

for num in sorted_list:
    print(num)
