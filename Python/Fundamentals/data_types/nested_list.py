# arr=[["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39],["John",39]]
# scores=[]
# for i in arr:
#     scores.append(i[1]) #scoress=[37.21,37.21,37.2,41,39]
# sorted_scores=sorted(list(set(scores))) #sorted_scores=[37.2,37.21,39,41]

# # sorted_scores=sorted(list(set(arr[i[1]] for i in arr)))
# lowest_score = sorted_scores[1] 
# alpha_names=[]
# for i in arr:
#     if i[1]== lowest_score:
#         alpha_names.append(i[0])
# alpha_names.sort()
# print(alpha_names)

if __name__ == '__main__':
    N=int(input( ))
    if N>=2 and N<=5:
        arr=[]   #arr = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 
        for i in range(N):
            name = input()
            score = float(input())
            arr.append([name, score])     
        scores=[i[1] for i in arr]     #scores=[37.21,37.21,37.2,41,39]
        sorted_scores=sorted(list(set(scores))) #[37.2,37.21,39,41]
        lowest_score = sorted_scores[1] #37.21
        alpha_names=[]
        for i in arr:
            if i[1]== lowest_score:
                alpha_names.append(i[0])
                
        alpha_names.sort()
        for i in alpha_names:    # print(i for i in alpha_names)  This is wrong since it is a generator expression not a loop
            print(i)
      
 