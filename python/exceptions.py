import sys

try:
    x = int(input(" input x: "))
    y = int(input(" input y: "))
except ValueError:
    print(" Invalid Input detected")
    exit(1)
finally:
    print("bye")

try:
    result = x/y
except ZeroDivisionError:
    print(" Invalid number value, zero cannot be divided")
    exit(1)
finally:
    print("Bybye")

print(f" result {result}" )
