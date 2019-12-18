import sys
import os
from functools import reduce
dict = {}
wordLen = []

if(len(sys.argv) != 2):
	print ("Invalid Arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[1].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

with open(sys.argv[1]) as file:
	for line in file:
		for word in line.split():
			dict[word] = dict.get(word,0) + 1
#print(dict)
sortedDict = sorted(dict.items(),key= lambda x:x[1],reverse=True)
for i in range(10):
    try:
        print(sortedDict[i])
    except IndexError:
        print("Has less than 10 words")   
        break
lst = []
#print(sortedDict[0][1]) 
for i in range(len(sortedDict)):
    lst.append(sortedDict[i][1])
print(lst) 
sum = reduce(lambda x,y: x+y,lst)
print('Avrg length :',sum/len(lst))    
lst1 = [x**2 for x in lst if x%2!=0]   
print(lst1)