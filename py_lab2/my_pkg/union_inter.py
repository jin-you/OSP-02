#! /usr/bin/python

def union_inter() :
	a=input("1st list : ")
	b=input("2nd list : ")

	list1=a.replace(" ", "").replace("[","").replace("]","").split(",")
	list2=b.replace(" ", "").replace("[","").replace("]","").split(",")

	union=[]
	inter=[]

	union.extend(list1)

	for i in list2 :
		if i in union :
			continue
		else :
			union.append(i)
	
	for i in list2 :
		if i in list1 :
			inter.append(i)
		else :
			continue
	
	union.sort()
	inter.sort()

	print(union)
	print(inter)

	return
	

if __name__=='__main__' :
	print("this is module")



