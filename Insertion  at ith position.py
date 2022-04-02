class Node: 

    def __init__(self, data): 
        self.data = data
        self.next = None # None is nothing but null 
        
class LinkedListInsertion: 

    # Whenever I'll create the object of a LinkedList class head will be pointing to null initially
    def __init__(self): 
        self.head = None

    def returnLastNode(self, n):
        temp = self.head
        c = 0
        iterations = 0
        while temp is not None:
            temp = temp.next
            iterations += 1
            c += 1

        p = self.head
        for i in range(c - n):
            iterations += 1
            p = p.next
        print("Iterations: ", iterations)
        return p.data

    def insertAtBeginning(self, key): 
        new_node = Node(key)  
        new_node.next = self.head 
        self.head = new_node 

    
    def insertAfter(self, nodeAfter, key): 

        h = self.head
        
        if h is None: 
            print ("The node can't be inserted in this case as the list doesn't exist.")
            return

        else:
            while h.data != nodeAfter:
                h = h.next
                if h is None:
                    print("The node can't be inserted")
                    return

            

            new_node = Node(key) 
            new_node.next = h.next
            h.next = new_node


    def insertionAtEnd(self, key): 

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
        while h is not None: 
            print (h.data, end = " -> ") 
            h = h.next
        print("None")



if __name__=='__main__': 

    myList = LinkedListInsertion()

    myList.insertionAtEnd(4)
    myList.insertionAtEnd(5)
    myList.insertionAtEnd(2)
    myList.insertionAtEnd(7)
    myList.insertionAtEnd(6)
    myList.printList()
    ans = myList.returnLastNode(2)
    print("Last 2nd Node:", ans)
