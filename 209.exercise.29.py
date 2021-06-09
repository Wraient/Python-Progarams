def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Please don\'t divide by zero"
    except TypeError:
        return "Please input numbers only"
    
    except:
        return "Unknown error ! "

print(divide(4,2))
print(divide(4,0))
print(divide("4",2))

