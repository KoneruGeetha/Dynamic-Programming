# Question:
# 1. You are given a number n, representing the number of stairs in a staircase.
# 2. You are on the 0th step and are required to climb to the top.
# 3. You are given n numbers, where ith element's value represents - till how far from the step you 
#      could jump to in a single move.  
#      You can of course jump fewer number of steps in the move.
# 4. You are required to print the number of different paths via which you can climb to the top
# Code:

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
dp=[0 for i in range(len(l)+1)]
dp[n]=1
j=len(l)-1
#print(dp)
for i in range(len(dp)-2,-1,-1):
    if (l[j]+i)<=n:
        dp[i]=sum(dp[i+1:i+l[j]+1])
        #print(dp[i],l[j],i)
        j=j-1
    else:
        dp[i]=sum(dp[i+1:n+1])
        #print(dp[i])
        j=j-1
print(dp[0])
