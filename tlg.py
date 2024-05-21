N = int(input())
max_lead = 0
leader = 0
lead = 0
for _ in range(N):
    score1, score2 = map(int, input().split())
    lead += score1 - score2
    if abs(lead) > max_lead:
        max_lead = abs(lead)
        leader = 1 if lead > 0 else 2

print(leader, max_lead)

