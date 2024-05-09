# Input
problems_solved = list(map(int, input().split()))
# Count the number of weeks
weeks_met_target = sum(1 for p in problems_solved if p >= 10)
# Output 
print(weeks_met_target)
