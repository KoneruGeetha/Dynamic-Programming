# Question:
# 1. You are given a number n, representing the count of elements.
# 2. You are given n numbers.
# 3. You are given a number "tar".
# 4. You are required to calculate and print true or false, if there is a subset the elements of which add 
#      up to "tar" or not.
# Code:

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
t=int(input())
dp=[[0 for i in range(t+1)]for j in range(len(l)+1)]
for i in range(len(l)+1):
    dp[i][0]=1
for i in range(1,len(l)+1):
    for j in range(1,t+1):
        if l[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=(dp[i-1][j] or dp[i-1][j-l[i-1]])
if dp[len(l)][t]==1:
    print("true")
else:
    print("false")
        
