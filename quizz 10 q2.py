__author__ = 'Eutimio'
def dotProduct (a1,b2):
	if (len(a1)) == len(b2):
		dotpro=0
		for y in range (0,len(a1)):
			x= a1[y]*b2[y]
			dotpro+=x
	else:
		print ("try again")
		return -1
	return (dotpro)



a1=[2,4,5,6]
b2=[1,2,3,4]
print(a1, "    ", b2)
print ("This program gives you the product dot of a list of 4 numbers")
total = dotProduct(a1,b2)
print ("The dot product is:", total)