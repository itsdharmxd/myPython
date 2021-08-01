class student:
    school="dharmesh school"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=self.m3+other.m3
        return student(m1,m2,m3)    
    def __str__(self):
        return f"{self.m1} {self.m2} {self.m3}"    
stu1=student(34,56,34)
stu2=student(87,12,45)
print(student.school)
stu1.school='lalit school'
print(stu1.school)
stu2.school='sneha school'
print(stu2.school)
stu3=stu1+stu2
print(stu3)        