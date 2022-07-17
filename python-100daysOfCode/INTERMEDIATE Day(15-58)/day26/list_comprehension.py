# input and output of list comprehension practice in python console


name = "Shubham" 
new_name = [letter + " " for letter in name] 
print(new_name)
['S ', 'h ', 'u ', 'b ', 'h ', 'a ', 'm '] 
new_name = [letter*3 for letter in name] 
print(new_name)
['SSS', 'hhh', 'uuu', 'bbb', 'hhh', 'aaa', 'mmm']   
final_numbers = [n*2 for n in range(1, 11)] 
print(final_numbers)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 
final_numbers= [n*2 for n in range(1, 20)] 
print(final_numbers)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38] 
a = [n for n in range(1, 20) if n % 2 == 0] 
print(a)
[2, 4, 6, 8, 10, 12, 14, 16, 18] 
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Fredddie"] 
names
['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Fredddie'] 


long = [n.upper() for n in names if len(n) > 5]  
long
['CAROLINE', 'ELANOR', 'FREDDDIE']
