# Print 1 to N Using Head Recursion 
def func(x,N):
    if x == N+1 :
        return
    print(x)
    func(x+1,N)
    
    
'''dry run

def func(1,4):
    if 1 == 4+1 :
        return
    print(1)
    func(2,4)

def func(2,4):
    if 2 == 4+1 :
        return
    print(2)
    func(3,4)
def func(3,4):
    if 3 == 4+1 :
        return
    print(3)
    func(4,4)

def func(4,4):
    if 4 == 4+1 :
        return
    print(4)
    func(4+1,4)

def func(5,4):
    if 5 == 4+1 :
        return
    print(x)
    func(x+1,N)'''