class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"{self.name} earns {self.salary}"

    def work(self):
        return "I am an Employee"
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def details(self):
        parent = super().details()
        return f"{parent} and works in {self.department}"

    def work(self):
        return "I am a Manager"
class SeniorManager(Manager):
    def __init__(self, name, salary, department, region):
        super().__init__(name, salary, department)
        self.region = region

    def details(self):
        parent = super().details()
        return f"{parent}, handling region {self.region}"

    def work(self):
        return "I am a Senior Manager"
sm = SeniorManager("Mohammed", 50000, "HR", "South India")

print(sm.work())
print(sm.details())
