

def outer(f):
    def inner():
        print("Before")
        f()
        print("After")
    return inner

@outer
def func():
    print("Func")

func()
# print("++++++++++++++++")
# outer(func)()
# print("========")
# #func=outer(func)
# func()
#
