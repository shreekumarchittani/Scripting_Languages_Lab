class Student:
    name = ''
    age = ''
    lst = []
    mylist = []
    def __init__(self,name,age,lst):
        self.name = name
        self.age = age
        self.lst = lst
    def display(self):
        print(self.name,'     ',self.age,'     ',self.lst)
    def accept(self):
        myname = input("Enter name")
        myage = input("Enter age")
        mymarks = list(map(str,input().split()))
        p = Student(myname,myage,mymarks)
        p.display()
obj = Student('a','12',[1,2,3])
obj.display()
obj.accept()        