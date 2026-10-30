def func1():
    print("Function1")
def func2():
    print("Function2")
def func3():
    print("Function3")

functionMap = {}
functionMap["F1"] = func1
functionMap["F2"] = func2
functionMap["F3"] = func3

functionMap["F2"]()

for f in functionMap:
    functionMap[f]()

