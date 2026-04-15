class Solution:
    def compress(self, chars: list[str]) -> int:       
        n=len(chars)
        read=0
        write=0

        while read<n :
            ch= chars[read]
            count=0

            while read<n and chars[read]==ch:
                count+=1
                read+=1
            chars[write]=ch
            write+=1
            if count > 1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write           
A= Solution()
print(A.compress(["a","a","b","b","c","c","c"]))