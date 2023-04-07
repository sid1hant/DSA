class Node:
    def __init__(self,value):
        self.value=value
        self.next=None



class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next


    def insertLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:

            if location ==0:
                newNode.next=self.head
                self.head=newNode

            elif location==-1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                order=0

                while order < location-1:
                    tempNode=tempNode.next
                    order +=1

                nextnode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextnode
                if tempNode==self.tail:
                    self.tail=newNode


    def traverse(self):
     if self.head== None:
       print("No elements")
     else:
       temp=self.head
       while temp is not None:
         print(temp.value)
         temp=temp.next


 
    def searchLL(self,nodeValue):
      if self.head==None:
        print("List not there")

      else:
        node= self.head
        while node is not None:
          if node.value==nodeValue:
            return node.value
          node=node.next

        return "The value not in the list"


L1=LinkedList()
L1.insertLL(1, 0)
L1.insertLL(2, 1)
L1.insertLL(3, 1)
L1.insertLL(4, 1)

print([node.value for node in L1])

L1.searchLL(5)
    
