import art


def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operators = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(art.logo)
  
  first_number = float(input("What is the first number?: "))
  for operator in operators:
      print(operator)
    
  is_continue = False
  
  while not is_continue:
    operator = input("Pick an operation: ")
    next_number = float(input("What is the next number?: "))
    
    calculation_function = operators[operator]
    answer = calculation_function(first_number, next_number)
    
    print(f"{first_number} {operator} {next_number} = {answer}")
  
    continue_calc = input("Type 'y' to continue calculating or type 'n' to start a new calculation or type 'q' to exit: ")
    
    if continue_calc == "y":
      first_number = answer
    elif continue_calc == "n":
      is_continue = True
      calculator()
    elif continue_calc == "q":
      is_continue = True
      

calculator()