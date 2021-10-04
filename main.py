#WRITE YOUR CODE IN THIS FILE

#define hasl
def hasL(w):
    
    #len given word and assign to variable

    for i in range(0,len(w)):
        if w[i] == "l":
           return True
    return False


    
        




#run function
print(hasL("alabama"))