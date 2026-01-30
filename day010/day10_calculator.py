# Calculator 

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator(num1=None):

    if num1 is None:
        num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    opr = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    answer = operations[opr](num1, num2)

    print(f"{num1} {opr} {num2} = {answer}")

    choice = input("Type 'y' to continue or 'n' to restart: ")

    if choice == "y":
        calculator(answer)     

    else:
        print("\n" * 3)
        calculator()           


calculator()

