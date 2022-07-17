# # 1st way
# total = 0
# for i in range(2,101,2):
#     total += i
# print(total)

# # 2nd way 
total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
print(total)