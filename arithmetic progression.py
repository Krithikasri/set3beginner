N,A,D=map(int,input().split())
w=0
for i in range(1,N+1):
	w=w+A
	A=A+D
print(w)
