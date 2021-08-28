Question:
1. You are given a number n, representing the count of items.
2. You are given n numbers, representing the values of n items.
3. You are given n numbers, representing the weights of n items.
3. You are given a number "cap", which is the capacity of a bag you've.
4. You are required to calculate and print the maximum value that can be created in the bag without overflowing it's capacity.
Note1 -> Items can be added to the bag even partially. But you are not allowed to put same items again and again to the bag.
Code:

n=int(input())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
wt=int(input())
k=[]
s=0
c=[]
for i in range(len(p)):
    k.append([w[i],p[i]/w[i]])
    c.append([p[i],p[i]/w[i]])
d=sorted(k,key=lambda t:t[1],reverse=True)
c=sorted(c,key=lambda t:t[1],reverse=True)
i=0
while i<len(d) and wt>0:
    a=d[i]
    d1=c[i]
    if a[0]<=wt:
        s=s+d1[0]
        wt=wt-a[0]
    else:
        break
    i=i+1
if wt>0:
    s=s+d1[0]*(wt)/a[0]
print(float(s))
