class Node: 

    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList: 
    
    
    def __init__(self): 
        self.head = None


    
    def append(self, key): 

        h = self.head

        if h is None:
            new_node = Node(key)
            self.head = new_node
        else:
            while h.next != None:
                h = h.next
            new_node = Node(key)
            h.next = new_node

    
    def startingOfLoop(self):
        fast = self.head
        slow = self.head
        isLoopFound = False

        if self.head is None:
            print("The list doesn't exist.")
            return

        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isLoopFound = True
                break

        if isLoopFound is True:
            slow = self.head
            while slow != fast:
                slow = slow.next
                fast = fast.next

        print(slow.data)
        


# Code execution starts here 
if __name__=='__main__': 

    myList = LinkedList() 
    myList.append(3)
    myList.append(4)
    myList.append(5)
    myList.append(6)
    myList.append(7)
    myList.head.next.next.next.next.next = myList.head.next.next
    myList.startingOfLoop()
