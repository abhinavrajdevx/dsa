class Node:
    def __init__ (self, data):
        self.data= data
        self.next= None

class stack:
    def __init__(self, data):
        self.head= Node(data)

    def push (self, data):
        new_node= Node(data)
        curr= self.head
        while (curr.next != None):
            curr= curr.next
        curr.next= new_node

    def pop (self):
        curr= self.head
        while (curr.next != None):
            prev= curr
            curr= curr.next
        prev.next= None

    def peek (self):
        curr= self.head
        while (curr.next != None):
            curr= curr.next
        return curr.data

    def traverse (self):
        curr= self.head
        while (curr != None):
            print(curr.data)
            curr= curr.next

def main ():
    st= stack(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.pop()
    print ("peek: ", st.peek())
    st.traverse()

main()