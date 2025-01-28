# HEAD RECURSION
count = 0


def func():
    if count == 4:
        return
    print("Uzair")
    count += 1
    func()


func()
