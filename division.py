def divide(numberOne, numberTwo):
    try:
        (int(numberOne) / int(numberTwo))
    except ZeroDivisionError:
        return("You cannot divide by zero")
    return(int(numberOne) / int(numberTwo))
  