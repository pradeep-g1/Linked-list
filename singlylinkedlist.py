class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def print_ll(self):
        if self.head is None:
            print("the LInkedlist is empty :")
        else:
            node=self.head
            while node:
                print(node.data,end="->")
                node=node.next
    def insertion(self,item,location):
        newnode=Node(item)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode
            else:
                index=0
                currnode=self.head
                while index<location-1:
                    currnode=currnode.next
                    index+=1
                nextnode=currnode.next
                currnode.next=newnode
                newnode.next=nextnode
    def deletion(self,location):
        if self.head is None:
            print("oops ! the linkedlist is empty :")
        elif self.head == self.tail:
            self.head=self.tail=None
            print("the node deleted and entire linked list empty !")
        else:
            if location==0:
                self.head=self.head.next
            elif location==1:
                firstnode=self.head
                while firstnode:
                    if firstnode.next==self.tail:
                        break
                    firstnode=firstnode.next
                firstnode.next=None
                self.tail=firstnode
            else:
                index=0
                currnode=self.head
                while index<location-1:
                    currnode=currnode.next
                    index+=1
                nextnode=currnode.next
                currnode.next=nextnode.next
    def searching(self,itemvalue):
        if self.head is None:
            print("the LInked list is empty")
        else:
            firstnode=self.head
            while firstnode is not None:
                if firstnode.data==itemvalue:
                    print("yes the value founds: ")
                firstnode=firstnode.next
sll=Linkedlist()
n=int(input("enter the numbers :"))
for i in range(n):
    x=int(input("enter the num: "))
    sll.insertion(x,1)
sll.print_ll()
print()
y=int(input("enter the item location: "))
sll.deletion(y)
sll.print_ll()
print()
ele=int(input("enter the element value: "))
sll.searching(ele)
