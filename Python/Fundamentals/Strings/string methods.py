
# For checking all character in string is alpha/numeric/alnum

# if __name__ == '__main__':
#     s="qA2"
#     print(True if s.isalnum() else False)
#     print(True if s.isalpha() else False)
#     print(True if s.isdigit() else False)
#     print(True if s.islower() else False)
#     print(True if s.isupper() else False)  

# For checking any character in string is alpha/numeric/alnum

if __name__ == '__main__':
    s="qA2"
    print(any (ch.isalnum() for ch in s)) 
    print(any (ch.isalpha() for ch in s)) 
    print(any (ch.isdigit() for ch in s)) 


