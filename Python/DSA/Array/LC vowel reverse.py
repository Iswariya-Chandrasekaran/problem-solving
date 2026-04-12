vowel="aeiouAEIOU"
s="IceCreAm"
att=[ch for ch in s if ch in vowel]
rev_att=att[::-1]
print(rev_att[0])