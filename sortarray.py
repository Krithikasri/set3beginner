N=int(input())
h=list(map(int,input().split()))
j=sorted(h)
for i in range(0,len(j)):
  print(j[i],end=" ")
