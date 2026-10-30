

functionMap = {}

def decorator(key):
    def wrapper(f):
        functionMap[key] = f
        return f
    return wrapper

@decorator("Fun!")
def fun():
    print("This is fun!")

@decorator("!Fun")
def notFun():
    print("This is not Fun!")

@decorator("Cats")
def cats():
    print("Cats are awesome!")


#functionMap["!Fun"]()


for f in functionMap:
    functionMap[f]()


