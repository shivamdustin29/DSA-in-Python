class Node: 

    def __init__(self, data): 
        self.data = data
        self.next = None # None is nothing but null 


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

    
    def printList(self): 
        h = self.head 
        while (h): 
            print (h.data, end = " ") 
            h = h.next
        print()

    
    def nthNodeFromEnd(self, nthNode):
        prev = self.head
        curr = self.head
        if self.head is None:
            print("The list doesn't exist.")
            return

        
        for i in range(nthNode):
            if curr is not None:
                curr = curr.next
            else:
                print(" nodes are not present in the linked list.")
                return

        
        while curr is not None:
            curr = curr.next
            prev = prev.next

       
        print(prev.data)



if __name__=='__main__': 

    myList = LinkedList() 
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.append(5)
    myList.append(6) 
    print("Original List is: ", end = " ")
    myList.printList()
    myList.nthNodeFromEnd(3)
