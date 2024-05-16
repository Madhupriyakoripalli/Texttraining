testcases = int(input())
lead = 0
for i in range(testcases):
    player1,player2 = map(int,input().split())
    if abs(player1 - player2) >= abs(lead):
        lead = player1-player2
        if lead>0:
            w = 1
        else:
            w = 2
print(w,abs(lead))