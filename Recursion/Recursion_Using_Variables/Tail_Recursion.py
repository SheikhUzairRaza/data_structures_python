# TAIL RECURSION
count = 0


def func():
    if count == 4:
        return
    count += 1
    func()
    print("Uzair")


func()


#dry run 
'''def func():
    if 0 == 4:
        return
    count += 1
    func()
    print("Uzair")
def func():
    if 1 == 4:
        return
    count += 1
    func()
    print("Uzair")
def func():
    if 2 == 4:
        return
    count += 1
    func()
    print("Uzair")
def func():
    if 3 == 4:
        return
    count += 1
    func()
    print("Uzair")
def func():
    if 4 == 4:
        return
    count += 1
    func()
    print("Uzair")'''