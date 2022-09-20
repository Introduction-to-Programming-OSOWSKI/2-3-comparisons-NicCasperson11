#WRITE YOUR CODE IN THIS FILE
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

def lessThan(x, y):
    if x < y:
        return True
    else:
        return False

def equalTo(x, y):
    if x == y:
        return True
    else:
        return False

def greaterOrEqual(x, y):
    if x >= y:
        return True
    else:
        return False

def lessOrEqual(x, y):
    if x <= y:
        return True
    else:
        return False

print(greaterThan(6, 10))
print(equalTo(23, 23))
print(lessOrEqual(99, 100))
print(lessOrEqual(100, 100))
print(lessOrEqual(101, 100))