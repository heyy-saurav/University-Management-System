class Person:

    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
    def to_dict(self):
       
        for i in self.id:
            if self.id[0]=='f':
                type = 'faculty'
            elif self.id[0]=='s':
                type = 'student'
            else:
                print("Please Enter Valid ID.")
                return
        d = {"ID":self.id,"Name": self.name,'Type': type}
        print(d)
        return type
class student(Person):
    def __init__(self, id, name,major):
        super().__init__(id, name)
        self.major=

name=input("Enter Name: ")
id=input("Enter the ID: ")
a=Person(id,name)
a.__str__()
a.to_dict()
if to_dict()=='student':
    

