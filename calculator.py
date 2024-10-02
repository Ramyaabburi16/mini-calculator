def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculation():
    n1=int(input("Enter first number:"))
    for symbol in operation_dict:
     print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an operation:")
        n2=int(input("Enter second number:"))
        calculator_function=operation_dict[op_symbol]
        output=calculator_function(n1,n2)
        print(output)

        should_continue=input(f"Enter 'yes' to continue calculation with{output}or 'new' to start a new calculation or 'N0' to exit").lower()
        if should_continue=='yes':
            n1=output
        elif should_continue=='new':
            continue_flase=False
            calculation()
        
        else:
            continue_flag=False
        print("bye")
print(calculation())