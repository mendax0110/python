#this is a simple Example of te usage of OHM's Law

def OHM(U = 0, I = 0, R = 0):
    if U == 0:
        result = I * R
        print(result) 
    elif I == 0:
        result = U / R
        print(result)
    elif R == 0:
        result = U / I
        print(result)
    else:
        print("ERROR") 
    
    return 0