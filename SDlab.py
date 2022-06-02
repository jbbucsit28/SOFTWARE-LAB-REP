# node structure
class Node:
  #constructor to create a new node
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  #constructor to create an empty LinkedList
  def __init__(self):
    self.head = None

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (True):
        print(temp.data, end=" ")
        temp = temp.next
        if(temp == self.head):
          break
      print()
    else:
      print("The list is empty.")

# test the code
# create an empty LinkedList
MyList = LinkedList()

#Add first node.
first = Node(10)
#linking with head node
MyList.head = first
#linking next of the node with head
first.next = MyList.head
#linking prev of the head
MyList.head.prev = first

#Add second node.
second = Node(20)
#linking with first node
second.prev = first
first.next = second
#linking next of the node with head
second.next = MyList.head
#linking prev of the head
MyList.head.prev = second

#Add third node.
third = Node(30)
#linking with second node
third.prev = second
second.next = third
#linking next of the node with head
third.next = MyList.head
#linking prev of the head
MyList.head.prev = third

#print the content of list
MyList.PrintList()