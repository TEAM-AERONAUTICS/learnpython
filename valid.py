def calculator(val):
    try:
        print(eval(val))
    except(ZeroDivisionError):
        return ("Cannot divide by zero!")
    except:
        return ("Error!")
        
calculator(input())
