def announce(f):
    def wrapper():
        print("About to start execution")
        f()
        print("Done with the execution")
    return wrapper

@announce
def hello():
    print(" Hellooooooooo")

hello()