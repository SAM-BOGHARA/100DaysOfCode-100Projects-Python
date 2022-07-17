# # exercise-1
# numbers = [1,1,2,3,5,8,13,21,34,55]

# a = [n*n for n in numbers]
# print(a)

# # exercise-2
# numbers = [1,1,2,3,5,8,13,21,34,55]


# a = [n for n in numbers if n % 2 == 0]
# print(a)

# exercise-3 ---to find similar integers in two diffferet lists and print it

file1 = "INTERMEDIATE/day26/file1.txt"
with open(file1, "r") as a:
    file1_data = a.readlines()

file2 = "INTERMEDIATE/day26/file2.txt"
with open(file2, "r") as b:
    file2_data = b.readlines()

results = [int(n) for n in file1_data if n in file2_data]

print(results)
