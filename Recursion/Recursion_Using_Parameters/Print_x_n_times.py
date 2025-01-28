#Using Head Recursion 
def fun(x,n):
    if n==0:
        return 
    print(x)
    fun(x,n-1)
fun(15,4)
# dry run 
# def fun(x=15,n=4):
#     if n==1:
#         return 
#     print(x)
#     fun(x,n-1)
# def fun(x = 15,n = 3):
#     if n==1:
#         return 
#     print(x)
#     fun(15,2)
# def fun(x=15,n=2):
#     if n==0:
#         return 
#     print(x)
#     fun(x,n-1)
# def fun(x=15,n=1):
#     if n==0:
#         return 
#     print(x)
#     fun(x,n-1)