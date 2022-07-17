logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# calculator functions
def add(n1, n2):
    return(n1 + n2)


def sub(n1, n2):
    return(n1 - n2)


def mul(n1, n2):
    return(n1 * n2)


def div(n1, n2):
    return(n1 / n2)

# dictionary


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    s = "Welcome to the Pythonic Calculator!"
    s = s.center(100,'*')

    print("\n" + s + "\n")
    print(logo)
    n1 = float(input("What's the first number :> "))

    for symbol in operations:
        print(symbol, end=' ')

    should_continnue =True


    while should_continnue:
        operation_symbol = input("pick an operation from above :^")
        n2 = float(input("What's the second number :> "))
        calculation_function = operations[operation_symbol]
        a = calculation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {a}")

        
        if input(f"Type 'y' to continue calculating with {a}, or type 'n' to start new calculator: \n").lower() == 'y':
            n1 = a
        else:
            should_continnue =False
            print(f"{n1} {operation_symbol} {n2} = {a}")
            calculator()

calculator()