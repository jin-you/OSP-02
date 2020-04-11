#! /usr/bin/python

n=int(input("몇 개의 숫자를 입력할 것인가? : "))
mysum=0

for i in range(0,n,1) :
	num=int(input("num :"))
	mysum+=num

average=mysum/n

print("average : %.2f" % average)

