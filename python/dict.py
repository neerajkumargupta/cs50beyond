words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r")
    try:
        for line in file:
            words.add(line.rstrip("\n"))
    finally:
        if file is not None:
            file.close()
    return True

def size():
    return len(words)

def upload():
    return True
