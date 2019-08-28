a = {}
while(True):
	print("Enter usn and name,-1 to exit")
	m = input()
	if m=='-1':
		break
	n = input()
	a[m] = n
temp = []	
'''I will append all the keys starting with 'a' to temp then 
using that list i will delete it from dictionary. The question 
arise that we can delete elements directly in the below loop.
If you do that you will get an error'''
for k,v in a.items():
	if v[0]=='a':
		temp.append(k)''' try del a[k] here. Delete the 
		next for loop to check whether direct deletion 
		works or not'''
for i in temp:
	del a[i]
lst = []	#For sorting append all the remaining names to a list
c = {}
for k,v in a.items():
	lst.append(v)
	c[v] = k
lst.sort()
b = {}
for i in lst:
	b[c[i]] = i	# c contains all the key values of names which are in alphabatical order
print(b)						
