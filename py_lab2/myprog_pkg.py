#! /usr/bin/python
import my_pkg

while True : 
	sel=input("Select menu: 1)conversion 2)union/intersection 3)exit ? ")
	
	if sel=="1" :
		my_pkg.converse()
	elif sel=="2" :
		my_pkg.union_inter()
	elif sel=="3" :
		break
