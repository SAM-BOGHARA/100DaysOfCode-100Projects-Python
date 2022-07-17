student_scores = input("Input a list of student heights :").split(' ')
for height in range(0, len(student_scores)):
    student_scores[height] = int(student_scores[height])
print(student_scores)

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"Highest score in the students is :{highest_score}")