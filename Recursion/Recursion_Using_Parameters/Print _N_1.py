# Print N to 1 using Head Rec 
print('Print N to 1 using Head Recursion')
def func(N):
    if N == 0 :
        return 
    print(N)
    func(N-1)
func(4)

# Print N to 1 using Tail Rec 
print('Print N to 1 using Tail Recursion')
def func(i,N):
    if i == N+1 :
        return 
    func(i+1,N)
    print(i)
func(1,4)
