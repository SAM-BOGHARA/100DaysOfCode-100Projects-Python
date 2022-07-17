year = int(input("which year do you want to check :"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# day13
# year = int(input("which year do you want to check :"))
# for year in range(2000,3000):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f"{year} is leap year")
#             else:
#                 print(f"{year} is not leap year")
#         else:
#             print(f"{year} is leap year")
#     else:
#         print(f"{year} is not leap year")
