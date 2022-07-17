student_heights = input("Input a list of student heights :").split(' ')
for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])
print(student_heights)

# total_student_heights = sum(student_heights)
# num_student_heights = len(student_heights)
# average_student_heights = round(total_student_heights/num_student_heights)
# print(average_student_heights)
total_student_heights = 0

for height in student_heights:
    total_student_heights += height

number_of_students = 0

for student in student_heights:
    number_of_students += 1

average_student_heights = round(total_student_heights / number_of_students)
print(f"Average height od student is : {average_student_heights}")
