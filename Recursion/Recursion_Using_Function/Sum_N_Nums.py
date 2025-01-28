#Print Sum of Natural Number (N)

def Nat_Sum(N):
    if N == 1:
        return 1 
    return N + Nat_Sum(N-1)

# def Nat_Sum(5):
#     if N == 1:
#         return 1 
#     return 5 + (Nat_Sum(4))=>10
# def Nat_Sum(4):
#     if N == 1:
#         return 1 
#     return 4 + (Nat_Sum(3))=>6
# def Nat_Sum(3):
#     if N == 1:
#         return 1 
#     return 3 + (Nat_Sum(2))=>3
# def Nat_Sum(2):
#     if N == 1:
#         return 1 
#     return 2 + (Nat_Sum(1))=>1
# def Nat_Sum(1):
#     if N == 1:
#         return 1 
#     return 1 + (Nat_Sum(0))

print(Nat_Sum(4))