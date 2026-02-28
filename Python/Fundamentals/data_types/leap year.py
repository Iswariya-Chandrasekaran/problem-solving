def is_leap(year):
    leap = False
    if year >=1900 and year <= 10**5:
        if year % 400 == 0 or (year % 4== 0 and year % 100 != 0):
            leap=True

    return leap
            

year = int(input())
print(is_leap(year))

# Wrong way 

# def is_leap(year):
#     leap = False
#     if year >=1900 and year <= 10**5:
#         if year % 4 == 0:
#              leap=True
#         elif year % 400== 0:
#             leap= True
#         elif year % 100 == 0:
#             pass
#     return leap
            

# year = int(input())
# print(is_leap(year))

#Corrected version - Always check for 400 first

# def is_leap(year):
#     leap = False
#     if 1900 <= year <= 10**5:
#         if year % 400 == 0:
#             leap = True
#         elif year % 100 == 0:
#             pass          # keep False
#         elif year % 4 == 0:
#             leap = True
#     return leap
