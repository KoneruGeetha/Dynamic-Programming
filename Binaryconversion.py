# Question:
# Printing N numbers in Binary Format.
# Code:

n=int(input())
dp=[0]*(n+1)
dp[1]=1
dp[2]=10
k=2
for i in range(3,n+1):
    if i&(i-1)==0:
        dp[i]=dp[i//2]*10
        k=i
    else:
        dp[i]=dp[i-k]+dp[k]
print(dp)
