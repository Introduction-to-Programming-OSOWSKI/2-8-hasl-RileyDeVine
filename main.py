#WRITE YOUR CODE IN THIS FILE

#define hasl
def hasL(w):
    
    #start at 0 and move through length of word
    for i in range(0,len(w)):
        #if letter at position equals l
        if w[i] == "l":
           return True
    return False

#run function
print(hasL("alabama"))