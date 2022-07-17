# import random as rd


# for i in range(1,100):
#     a.append(rd.randint(1,1000))

a = [183, 151, 20, 553, 607, 788, 351, 549, 803, 762, 770, 475, 842, 457, 635, 422, 735, 382, 778, 762, 229, 224, 250, 327, 787, 801, 480, 689, 584, 552, 278, 202, 970, 470, 502, 955, 35, 232, 921, 26, 752, 338, 217, 222, 306, 140, 808, 369, 419, 825, 162, 998, 146, 786, 997, 155, 696, 996, 582, 629, 191, 5, 252, 463, 803, 148, 81, 259, 404, 524, 588, 625, 776, 681, 557, 541, 955, 471, 883, 809, 849, 535, 242, 286, 499, 717, 789, 36, 13, 571, 340, 45, 393, 276, 902, 229, 886, 706, 825]

print(f"the unsorted list is :{a}")
def bubblesort(a):
    for i in range(0,len(a)-1): 
        for j in range(0,len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return f"{a}"

print("================================================")
print(f"The Bubble sorted list is :{bubblesort(a)}")


def insertion_sort(a):
    for i in range(1, len(a)): 
            key = a[i]
            j = i-1
            while j >= 0 and key < a[j] : 
                    a[j + 1] = a[j] 
                    j -= 1
            a[j + 1] = key
    return a
print("================================================================")
print(f"The Insertion sorted list is :{insertion_sort(a)}")