x = 5
y = 1

try:
    z = x / y
    print("save me")
except ZeroDivisionError:
    print("You cannot devide by zero")
    exit(1)
finally:
    print("hows that possible") 
