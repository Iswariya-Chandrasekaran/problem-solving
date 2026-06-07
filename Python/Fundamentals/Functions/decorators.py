def  great_check(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@great_check
# After decoration, divide actually becomes inner. calling divide(4,2) ==inner(4,2)
def divide(a,b):
    return int(a/b)

print(divide(4,2))
print(divide(2,8))
# ---------------------

def changecase(funct):
    def myinner(name,*args,**kwargs):
        return funct(name,*args,**kwargs).upper()
    return myinner
    

@changecase    
def preparing(name,*args,**kwargs):
    age=args[0]
    role=kwargs["role"]
    return f"Im {name}  and {age} preparing for {role} interviews"

print(preparing("Isu", 21,23, role="Backend"))

# ---------------
def A(func):
    def wrapper():
        print("A before")
        result = func()
        print("A after")
        return result
    return wrapper

def B(func):
    def wrapper():
        print("B before")
        result = func()
        print("B after")
        return result
    return wrapper

@A
@B
def hello():
    print("hello")

hello()

# ---------------------
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# 
import functools
def changecase(func):
    @functools.wraps(func)
    def wrap():
        return func().upper()
    return wrap

@changecase
def intro():
    return "Im Iswariya"

print(intro.__name__)

# A decorator factory that takes an argument and transforms the casing based on the argument value.
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())