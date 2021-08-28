# Question:
# 1. You are given a number n, representing the number of elements.
# 2. You are given a number k, representing the number of subsets.
# 3. You are required to print the number of ways in which these elements can be partitioned in k non-empty subsets.
# E.g.
# For n = 4 and k = 3 total ways is 6
# 12-3-4
# 1-23-4
# 13-2-4
# 14-2-3
# 1-24-3
# 1-2-34
# Code:
n=int(input())
k=int(input())
dp=[[0 for i in range(k+1)]for j in range(n+1)]
for i in range(n+1):
    dp[i][0]=0
    dp[i][1]=1
for j in range(k+1):
    dp[0][j]=0
for i in range(1,n+1):
    for j in range(1,k+1):
        if i==j:
            dp[i][j]=1
        else:
            dp[i][j]=(j)*dp[i-1][j]+dp[i-1][j-1]
print(dp[n][k])
