# ==========================================
# B201 Computer Science Lab - Exercise
# Student Name: Arjaf Anwar
# Project: Simple Course Grade Calculator
# ==========================================

# 1. Store assignment points in variables
math_score = 85
programming_score = 90
english_score = 75

# 2. Calculate the average score using basic operators
total_score = math_score + programming_score + english_score
average_grade = total_score / 3

# 3. Print the results to the screen
print("=== STUDENT GRADE REPORT ===")
print("Mathematics Mark:", math_score)
print("Programming Mark:", programming_score)
print("English Mark:    ", english_score)
print("----------------------------")
print("Average Grade:   ", average_grade)
print("============================")

# 4. Check if the student passed using if/else control flow
if average_grade >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
