mylist = [1,45,2,3,4,6,7,8]
temp = None
for i in range(len(mylist)):
	temp = mylist[i]
	if mylist[i] != mylist[-1] and mylist[i] > mylist[i+1]: 
		break
		
print(f"The first element greater than the next one is: {temp}")
