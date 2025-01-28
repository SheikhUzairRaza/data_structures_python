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
    
# Tail Recursion Backtracking
def func(N):
    if N>0 :
        return
    func(N-1)
    print(N)
'''dry run
def func(4):
    if 4>0 :
        return
    func(3)
    print(4)
def func(3):
    if 3>0 :
        return
    func(2)
    print(3)
def func(2):
    if 2>0 :
        return
    func(1)
    print(2)
def func(1):
    if 1>0 :
        return
    func(0)
    print(1)
def func(0):
    if 0>0 :
        return
    func(-1)
    print(0)''''''
    