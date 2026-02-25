class Employee:
    # Constructor of parent  class
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        #  print(f"{self.name} salary is {self.salary}")
        return f"My salary is {self.salary}"
         
    def work(self):
        return "I am an Employee"
    
class Manager(Employee):
    #Extending the parent class constructor
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    
    #Extending the parent class details method
    def details(self):
        parent=super().details()
        return f" {parent}. I'm working in this {self.department} department"
    
    # Overriding the parent class work method
    def work(self):
        return f"I'm  Manager {self.name}"

Manager1 = Manager("Mohammed",20000,"HR Finance")
print(Manager1.work())
print(Manager1.details())