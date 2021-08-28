# Question:
# 1. You are given a number n, representing the number of rows.
# 2. You are given a number m, representing the number of columns.
# 3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
# 4. You are standing in top-left cell and are required to move to bottom-right cell.
# 5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
# 6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom- 
#      right cell).
# 7. You are required to traverse through the matrix and print the cost of path which is least costly.
# Code:

n=int(input())
m=int(input())
l=[]
for i in range(n):
    c=list(map(int,input().split()))
    l.append(c)
dp=[[0 for i in range(m)]for j in range(n)]
dp[0][0]=l[0][0]
for i in range(1,len(l)):
    dp[i][0]=dp[i-1][0]+l[i][0]
for j in range(1,len(l[0])):
    dp[0][j]=dp[0][j-1]+l[0][j]
for i in range(1,len(l)):
    for j in range(1,len(l[0])):
        dp[i][j]=l[i][j]+min(dp[i-1][j],dp[i][j-1])
print(dp[len(l)-1][len(l[0])-1])
