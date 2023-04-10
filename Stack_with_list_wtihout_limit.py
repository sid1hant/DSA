class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values= reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            False

    def push(self,value):
        self.list.append(value)
        return "The element addded"


    def pop(self):
        if self.isEmpty():
            return "There is not a element "
        else:
            return self.list.pop()
   
     
    def peek(self):
        if self.isEmpty():
            return "There is not a element "

        else:
            return self.list[len(self.list)-1]




s=Stack()
s.push(1)
s.push(4)
s.push(6)
s.pop()
print(s.peek())
print(s)
