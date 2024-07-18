#simple sys company:
class campany():
    def __init__(self,name,age,job,national,salary):
        self.name = name
        self.age = age
        self.job = job
        self.national = national
        self.salary = salary

    #to calcute taraget:
    def taragetsalary(self,taraget):
        taragetsalary = taraget + self.salary 
        print('taragetsalary  = ' ,  taragetsalary)   

    #function to print all : 
    def printall(self):
        print('name = ' , self.name) 
        print('age = ' , self.age) 
        print('job = ' , self.job) 
        print('national = ' , self.national) 
        print('salary = ' , self.salary)  


emp1=campany('manar',23,'programmer','egypt',2000)
emp1.taragetsalary(3000)
emp1.printall()

emp2=campany('ahmed',30,'programmer','egypt',1500)
emp1.taragetsalary(2300)
emp1.printall()

emp1=campany('mahamed',35,'programmer','egypt',4000)
emp1.taragetsalary(1200)
emp1.printall()

emp1=campany('nor',25,'programmer','egypt',1000)
emp1.taragetsalary(200)
emp1.printall()
        