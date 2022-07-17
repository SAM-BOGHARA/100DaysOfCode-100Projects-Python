from prettytable import PrettyTable
table = PrettyTable()
table.add_column('name',['shubham','shubh','sam','batman','python'])
table.add_column('id',[1,2,3,3,5.5])

table.align = 'l'
print(table)
