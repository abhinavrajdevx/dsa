class node:
    def __init__(self, data):
        self.data= data
        self.next= None

class linked_list:
    def __init__(self, data):
        self.head= node(data)
    
    def append (self, data):
        new_node= node(data)
        curr= self.head
        while (curr.next != None):
            curr= curr.next
        curr.next= new_node

    def appendAtBegin (self, data):
        new_node= node(data)
        new_node.next=self.head
        self.head= new_node

    def appendAtEnd (self, data):
        curr= self.head
        new_node= node(data)
        while (curr.next != None):
            curr= curr.next
        print('LAst noe: ', curr.next)
        curr.next= new_node
        print('LAst noe: ', curr.next)

    def appendAtPosition (self, index, data):
        curr= self.head
        prev= None
        new_node= node(data)
        _index= 0
        while (curr != None):
            if (_index == index):
                new_node.next= curr
                if (prev != None):
                    prev.next= new_node
                elif (prev == None):
                    self.appendAtBegin(data)
                return True
            prev= curr
            curr= curr.next
            _index= _index+1
        return False
    
    def find(self, data):
        curr= self.head
        while (curr != None):
            if (curr.data == data):
                return True
            curr= curr.next
        return False
    
    def traverse (self):
        curr= self.head
        while (curr != None):
            print(curr.data)
            curr= curr.next

    def remove(self, index):
        _index= 0
        curr= self.head
        prev= None
        while (curr != None):
            if (index == _index):
                if (prev != None):
                    prev.next= curr.next
                elif (prev == None):
                    self.head= curr.next
            prev= curr
            curr= curr.next
            _index= _index +1

    def get_head(self):
        head= self.head
        return head.data
    
def main ():
    list1= linked_list(0)
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list1.append(4)
    list1.append(5)
    list1.appendAtBegin(99)
    list1.appendAtBegin(97)
    list1.appendAtEnd(77)
    list1.remove(3)
    list1.appendAtPosition(0, 1000)
    list1.appendAtPosition(8, 9000)
    list1.traverse()
    print(list1.find(1))
    print(list1.get_head())

main()