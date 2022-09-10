#code
def primeFactor(N):
    nums = [2,3,5,7]
    primeF = []
            
    while N > 1:
       for i in range(len(nums)):
           if N % nums[i] == 0:
               primeF.append(nums[i])
               N = N//nums[i]
    return len(primeF)

def HCF(X, Y):
    if X > Y:
        while Y:
            X, Y = Y, X % Y
        return X    
        
    elif Y > X:
        while X:
            Y, X = X, Y % X
        return Y

        
def WierdElevator(X,Y,M):
    hcf = HCF(X, Y)
    num1 = X // hcf
    num2 = Y // hcf
    a = primeFactor(num1)
    b = primeFactor(num2)
    return (a+b, hcf)
    
    


print(WierdElevator(160,180,10))
