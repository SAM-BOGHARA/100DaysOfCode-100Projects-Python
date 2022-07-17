# new_dict = {new_key: new_value for new_key, new_value in list if test}


import random
names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]

names_dict = {student: random.randint(1, 100) for student in names}
# print(names_dict)


passed_student = {students: marks for (
    students, marks) in names_dict.items() if marks >= 55}
print(passed_student)
