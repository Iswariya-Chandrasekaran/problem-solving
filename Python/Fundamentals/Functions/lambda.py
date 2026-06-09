users = [
    {"name":"Anbu","salary":20000,"active":False},
    {"name":"Banu","salary":40000,"active":True},
    {"name":"Cathy","salary":30000,"active":True},
]

# Sorting through salary
x_sort = sorted(users,key=lambda user: user["salary"])
print(x_sort)

# filtering and mapping(transforming the records to list) 

x_filter = list(filter(lambda user:user["active"]==True, users))
print(x_filter)

active_names = list(map(lambda user:user["name"],x_filter))
print(active_names)

#get cathy salary from salary list
cathy_salary=lambda user:user["salary"]
print(cathy_salary(users[2]))

# lambda func passed as param Instead of new function since used only once
def get_salary(user):
    return user["salary"]

print(get_salary(users[2]))