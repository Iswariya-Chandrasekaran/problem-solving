class solution:
    def str_hcf(self, str1:str, str2:str)-> str:
      # 1. check is both str follows same pattern if not no gcd exists
      # ABABAB + ABAB == ABAB + ABABAB
      # AAAAAB + AAA != AAA + AAAAAB
        if str1+str2 != str2+str1:
            return ""
        # 2. Find GCD with the len of both strings
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        ans=gcd(len(str1),len(str2))
        # 3. Return substring of that length
        return str1[:ans]
A= solution()
print(A.str_hcf("ABCABC","ABC"))
            