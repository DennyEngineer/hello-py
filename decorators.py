def announce(f):
    def wrapper():
        print("Your function is about to be run")
        f()
        print("function was run successfully")
    return wrapper

@announce
def Hello():
    print("hello world")

Hello()

