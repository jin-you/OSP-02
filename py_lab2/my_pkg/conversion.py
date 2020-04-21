#! /usr/bin/python

def converse() : 
	a=input("input binary number : ")
	x=int(a,2)

	print("=>OCT> %o\n=>DEC> %d\n=>HEX> %X"%( x, x, x))
	
	return

if __name__=='__main__' :
	print("this is module")
