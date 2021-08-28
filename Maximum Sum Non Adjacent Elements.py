# Question:
# 1. You are given a number n, representing the count of elements.
# 2. You are given n numbers, representing n elements.
# 3. You are required to find the maximum sum of a subsequence with no adjacent elements.
# Code:
 
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
dp=[[0 for i in range(n)]for j in range(2)]
dp[0][0]=l[0]
for j in range(1,len(l)):
    dp[0][j]=dp[1][j-1]+l[j]
    dp[1][j]=max(dp[1][j-1],dp[0][j-1])
print(max(dp[0][n-1],dp[1][n-1]))
            
