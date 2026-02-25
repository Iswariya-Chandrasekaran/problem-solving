thickness = int(input())  # must be odd
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*(2*i+1)).center(thickness*2))
    # print(" "*(thickness-i) + c*(2*i-1))