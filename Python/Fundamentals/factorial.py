# def factorial(n):
#     if n==1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))
# -----------------------
# n= 5
# i=n
# x=1
# while i > 0 :
#     x= x*i
#     i=i-1
# print(x)


def numbers(n):
    if n == 0:
        return 
    numbers(n-1)
    print(n, end ="")

# n = int(input("Enter number:"))
numbers(3)