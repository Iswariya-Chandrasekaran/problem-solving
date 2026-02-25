if __name__ == '__main__':
    # To get the number of students' records.
    n = int(input())
    if not (2<=n<=10):
        raise ValueError("Number of students must be between 2 and 10")
    
    student_marks = {} # To store the records

    # Loop to get records 
    for i in range(n):
        #takes a single line of input from the user, splits it into separate words based on
        #  whitespace and assigns the first word to the variable name and all the remaining words to a list called line
        name, *line = input().split()
        scores = list(map(float, line))

        if len(scores)!=3:
             raise ValueError("Each student must have exactly three scores")
        
        if not all(0<=mark<=100 for mark in scores):
            raise ValueError("Scores must be between 0 and 100")     
                                                  
        student_marks[name] = scores
    query_name = input()        
    if query_name not in student_marks:
        raise ValueError("Student not found")

    avg=sum(student_marks[query_name])/len(student_marks[query_name])        
    print(f"{avg:.2f}")
                    
