
def decorator(x):
    def wrapper():
        print("start work")
        x()
        print("stop work")
    return wrapper

# def original_fun():
#     print("this is original")

# var=decorator (original_fun)
# #wrapper()
# var()

@decorator
def original_fun():
    print("this is original")

original_fun()