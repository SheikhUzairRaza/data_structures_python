#Print Sum of Natural Number (N)

def func(sum,i,N):
    if i > N :
        print(sum)
        return 
    func(sum + i , i + 1,N)
    
func(0,1,5)

# N*(N+1)/2  => (N=5) => 5*(5+1)/2 => 5*6/2 => 5*3 => 15 