class StackArray:

    
    MAX = 5

    stack = []    
    
    
    def __init__(self):
        self.top = -1

  
    def isEmpty(self):
        if(self.top < 0):
            return True
        return False

    
    def isFull(self):
        if(self.top >= self.MAX - 1):
            return True
        return False




    def push(self, key):

        if(self.isFull()):
            print("Stack Overflow")
            return False

        
        self.top += 1
        self.stack.append(key)
        print("The element is pushed and top points to => ",self.stack[self.top])
        return True

    
    def pop(self):
       
        if(self.isEmpty()):
            print("Stack underflow")
            return -1

        
        deletedElement = self.stack[self.top]
        self.top -= 1
        print(deletedElement)
        return deletedElement
    

   
    def peek(self):
        if(self.isEmpty()):
            print("There is no record in the stack.")
            return -1

        peekElement = self.stack[self.top];
        return peekElement;

if __name__ == '__main__': 
    s = StackArray()
    s.push(10) # now top is 10
    s.push(20) # now top is 20
    s.push(30) # now top is 30
    s.push(40) # now top is 40
    s.push(50) # now top is 50
    s.push(60) # Stack Overflow
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print("Top element is: " , s.peek())
    s.pop()
    print("Top element is: " , s.peek())
    s.pop()
    temp = s.pop() # after performing pop, top will point to 20 again.
    print("Deleted element is: ", temp)
