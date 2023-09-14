from art import logo
# Add function
def add(n1, n2):
    return n1 + n2
# Subtract function
def subtract(n1, n2):
    return n1 - n2
# Multiple Function
def multiple(n1, n2):
    return n1 * n2
# Divide Function
def divide(n1, n2):
    return n1 / n2
# Dictionary for operators
operators = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiple}

# Number 1 input
def calculator():
  print(logo)
  # Continue Flag
  calc_flag = True
  num1 = float(input("What is the first number: "))
  # Print operators
  for op in operators:
      print(op)
  while calc_flag == True:
    # Get operator symbol
    operator_symbol = input("Pick an operator from the line above: ")
    # Number 2 input
    num2 = float(input("What is the second number: "))
    # Get function
    function = operators[operator_symbol]
    # Get answer
    answer = function(num1, num2)
    # Print values and answer 
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    continue_calculation = input("Do you want to continue? Y or N to start a new calculation").lower()
    if continue_calculation == "y":
      num1 = answer
    else:
      calc_flag = False
      calculator()
calculator()
