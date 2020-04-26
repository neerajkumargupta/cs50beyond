from sys import argv, exit

if len(argv) < 3:
    print("missing commange line Args")
    exit(1)

for arg in argv:
    print(arg)
exit(0)
    