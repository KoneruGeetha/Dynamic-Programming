# Question:
# 1. You are given a number n, representing the count of items.
# 2. You are given n numbers, representing the values of n items.
# 3. You are given n numbers, representing the weights of n items.
# 3. You are given a number "cap", which is the capacity of a bag you've.
# 4. You are required to calculate and print the maximum value that can be created in the bag without 
#      overflowing it's capacity.

# Note -> Each item can be taken 0 or 1 number of times. You are not allowed to put the same item 
#                again and again
# Code:

n=int(input())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
wt=int(input())
dp=[[0 for i in range(wt+1)]for j in range(len(w)+1)]
for i in range(1,len(w)+1):
    for j in range(1,wt+1):
        if w[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
print(dp[len(w)][wt])
