# Question:
# 1. You are given a number n, representing the count of coins.
# 2. You are given n numbers, representing the denominations of n coins.
# 3. You are given a number "amt".
# 4. You are required to calculate and print the number of combinations of the n coins using which the 
#      amount "amt" can be paid.

# Note1 -> You have an infinite supply of each coin denomination i.e. same coin denomination can be 
#                   used for many installments in payment of "amt"
# Note2 -> You are required to find the count of combinations and not permutations i.e.
#                   2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same 
#                   combination. You should treat them as 1 and not 3.
# Code:

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
s=int(input())
dp=[[0 for i in range(s+1)]for j in range(len(l)+1)]
for i in range(len(l)+1):
    dp[i][0]=1
for i in range(1,len(l)+1):
    for j in range(1,s+1):
        if l[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j]+dp[i][j-l[i-1]])
print(dp[len(l)][s])
