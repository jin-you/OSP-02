#! /usr/bin/python

n=int(input("생성할 피보나치 수는? : "))

fibo=[1,1]

for i in range(0, n-2, 1) : 
	fibo.append(fibo[i]+fibo[i+1])
print(fibo)	
print("F%d=%d"%(n,fibo[n-1]))
