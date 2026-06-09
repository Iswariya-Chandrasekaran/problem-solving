students = {
    "Iswariya": {"score": 95, "grade": "A"},
    "Ravi":     {"score": 0,  "grade": "C"},
    "Meena":    {"score": 78, "grade": "B"},
}
students["Arun"]={"score": 5, "grade": "F"}

class LowScoreError(Exception):
    pass

#task 3
def get_score(students,name):
    try:
        score=students[name]["score"]
        if score < 10:
            raise LowScoreError("Student score is below 10")
    except KeyError:
        print("student name doesn't exist in the dictionary")
    except LowScoreError as e:
        print(f"custom error: {e}")
    else:
        print(f"result {score}")
    finally:
        print(f"Processing complete for: {name}")

get_score(students,"Iswariya")
get_score(students,"Karthick")
get_score(students,"Arun")

#task 2
def get_ratio(students, name, total):
    try:
        ratio=students[name]["score"] / total
    except KeyError:
        print("student name doesn't exist in the dictionary")
    except ZeroDivisionError:
        print("can't be divisble by zero")
    except TypeError:
        print("object of the wrong data type")
    else:
        print(ratio)

get_ratio(students, "Iswariya", 100)
get_ratio(students, "Ravi", 0)
get_ratio(students, "Meena", "hundred")
get_ratio(students, "Karthik", 100)