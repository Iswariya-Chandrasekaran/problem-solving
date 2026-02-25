class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"
class Developer(Employee):
    def work(self):
        return "Writing code..."

dev = Developer("Ice", 15000)

print(dev.get_details())   # inherited method
print(dev.work())    # child-specific method
print(isinstance(dev, Employee))  # True
print(isinstance(dev, Developer))  # True