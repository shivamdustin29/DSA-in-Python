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

    def deleteNode(self, key):
        h = self.head
        prev = None

        if h is None:
            print("The list is empty, the node can't be deleted.")
            return

        if h.data == key:
            self.head = h.next
            return

        while h is not None and h.data != key:
            prev = h
            h = h.next

        if h is None:
            print("The key is not present in the list.")
            return

        prev.next = h.next


if __name__=='__main__': 

    myList = LinkedList() 
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.append(6)
    myList.append(7) 
    print("Original List is: ", end = " ")
    myList.printList()
    myList.deleteNode(6)
    print("After Deletion: ", end = " ")
    myList.printList()
