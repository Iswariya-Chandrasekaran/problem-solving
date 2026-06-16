class solution:
    def reverseonlyvowel(self, s:str)->str:
        # Getting only vowels from str as a array
        vow_arr=[ch for ch in s if ch in "aeiouAEIOU"]
        #reversed will take both str,arr but returns only iterator obj. so use list()/join
        # reversing the array of vowels
        rev_vow_arr=list(reversed(vow_arr))
        # Making the input str as list
        s_arr=list(s)
        # index for replacing since both arr length will differ
        rev_vow_arr_idx=0

        for i in range(len(s_arr)):
            if s_arr[i] in "aeiouAEIOU":
               s_arr[i]= rev_vow_arr[rev_vow_arr_idx]
               rev_vow_arr_idx+=1
        return "".join(s_arr)

A=solution()
print(A.reverseonlyvowel("IceCreAm"))
