# y=True
# while y ==True:
#     try:
#         x = input("Enter your name:")
#         if not x.isdigit():
#             print("Hello," ,x)
#             y=False
#     except:
#         print(x, "Please Enter valid name")
# print("Thanks for the Valid input")


# n=4
# for i in range(n):
#     print(("G"*(2*i+1)).center(10))
# for i in range(n-1):
#     print(("H"*7).center(10)+ ("H"*7).rjust(10))
# for i in range(n):
#     print(("G"*(n-i)).rjust(20))

t=int(input())
for i in range(t):
    print(("H"*(2*i+1)).center(t))