class Reversing:
    sent = ""
    vowels = ['a','e','i','o','u']
    def __init__(self,sentence):
        self.sent = sentence
    def reverse(self):
        lst = self.sent.split()
        lst.reverse()
        return lst
    def getVowelCount(self,mystr):
        count=0
        for item in mystr:
            if item in self.vowels:
                count = count + 1
        return count   
    def vowelCount(self):
        lst = self.sent.split()
        dict = {}
        for i in range(len(lst)):
            count=0
            mystr = lst[i]
            for item in mystr:
                if item in self.vowels:
                    count+=1
            dict[lst[i]] = count 
        sortedDict = sorted(dict.items(),key=lambda x: x[1],reverse=True)
        return sortedDict
obj = Reversing('i am here because of you')
print(obj.reverse())
print(obj.vowelCount())