
from unittest import case

"""
node class 
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
class for the Linked list. Uses the Node class for the nodes. This Linked List is 
made like a linked list in C++ would be made, with curr, prev, and head nodes.
(object oriented programming!!!)
"""
class LinkedList:
    def __init__(self):
        self.head = None

    """
    function that appends a user inputed interger value into a new node. Uses an
    if statement to check if it is an empty list, as well as a while loop to move through
    the list and add a node.
    """
    def append(self, data):
        newNode = Node(data)
        if not self.head: # bool expression to determine if the list is empty, if yes the head is newNode
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    """
    Function to view the nodes in the Linked list. Uses if and while loops. 
    The first if statement checks if the head is null pointer using not, and the
    while loop prints the list.
    """
    def viewLL(self):
        if not self.head:
            print("The list is currently empty!")
            return
        index = 0
        curr = self.head
        while curr:
            print(f"{index}: {curr.data}")
            curr = curr.next
            index += 1

    """
    Function that removes a node in the Linked List. uses if, else, and while loops. 
    checks for empty list, and index. Removes the node selected by user by using 
    head, curr and prev pointers.
    """
    def removeNode(self, index):
        if not self.head:
            print("The list is empty!")
            return
        if index == 0:
            print(f"Removing: {self.head.data} ...")
            self.head = self.head.next
            return
        prev = None
        curr = self.head
        i = 0
        while curr and i < index: #short circuit evaluation to move the items around
            prev = curr
            curr = curr.next
            i += 1
        if curr:
            print(f"Removing: {curr.data} ...")
            prev.next = curr.next
        else:
            print("Index out of range!")

    """
    Function that clears the linked list. It clears the head, and the remaining 
    nodes are deleted automatically when nothing is pointing to them.
    """

    def clear(self):
        self.head = None

    """
    Function for the Linked List data structure (uses tail, head, curr, and prev
    pointers to select node values.) Returns the statues of the list (its empty).
    """

    def isEmpty(self):
        return self.head is None

"""
Main menu that is printed to the console. Displayed for both types of data structures
available.
"""
def printMenu():
    print()
    print("Welcome to the Interger and String storer")
    print("-----------------------------------------")
    print("1. Add intergers to the list")
    print("2. Add strings to the list")
    print("3. View linked list")
    print("4. Remove a specific node in the list")
    print("5. Clear the list")
    print("6. Exit the program")

"""
function used to add data to the python list (dynamic array). only runs if user chooses
python list as their data structure. Uses while loop, if, else, as well as 
a try except block to check for valid data types to be entered into the python
list by the user.
"""
def addData(lst, dataType, isLinked):
    print(f"Enter {dataType.__name__}s (enter -999 to stop):")
    while True:
        entry = input("> ").strip() #cool thing that cleans whitespace!
        if entry == "-999":
            break
        #type checking using try except block
        try:
            value = dataType(entry)
            if isLinked:
                lst.append(value) #appending item to python list
            else:
                lst.append(value)
        except ValueError:
            print(f"Invalid {dataType.__name__}. Try again!")

"""
function used to view the python list (dynamic array). only runs if user chooses
python list as their data structure. uses if, elses  as well as a 
for loop to view the list. the forloop uses enumerate, which is a built
in function that returns the contents of a list (in this case the dynamic array), 
as well as the index.
"""
def viewList(lst, isLinked):
    if isLinked:
        lst.viewLL()
    else:
        if not lst:
            print("The list is currently empty!")
        else:
            for i, val in enumerate(lst):
                print(f"{i}: {val}")

"""
function used to remove the node at a user specific index when user
desides to use the python list (dynamic array). Checks to make sure 
user inputs proper interger index using if, elif and else statements.
"""
def removeNode(lst, isLinked):
    index = input("Enter the index to remove the node: ")
    if index.isdigit():
        idx = int(index)
        if isLinked:
            lst.removeNode(idx)
        elif 0 <= idx < len(lst):
            print(f"Removing: {lst[idx]} ...")
            del lst[idx]
        else:
            print("Index out of range!")
    else:
        print("Invalid input!")

def clearList(lst, isLinked):
    if isLinked:
        lst.clear() #clearing the python list
    else:
        lst.clear()

"""
(cool way of making multi-line comments). Function that runs the main menu for this program.
Uses if, elif (else if), else and break inside of a while loop that uses a bool to gather user
input.
"""
def runMenu(lst, isLinked):
    while True:
        printMenu()
        choice = input("Enter your choice (1,2,3,4,5,6): ")
        print()
        # needs to download at least python 3.10 or newer for match to work (C++ switch statement equivalent) 
        match choice:
            case '1':
                addData(lst, int, isLinked)
            case '2':
                addData(lst, str, isLinked)
            case '3':
                viewList(lst, isLinked)
            case '4':
                removeNode(lst, isLinked)
            case '5':
                clearList(lst, isLinked)
            case '6':
                print("Good Bye!")
                break
            case _: #'case _: is the default case.
                print("Invalid choice. Try again!")

"""
function that displays a small menu which prompts the user on which data structure they 
want to use to store their ints and strings. uses the same while loop and if else statements 
as the main menu.
"""
def main():

    print("Welcome to the Interger and String storer")
    print("-----------------------------------------")
    print("1. Use Linked List")
    print("2. Use Python list (dynamic array)")

    while True:
        Dstruct = input("Choose Data Structure (1 or 2): ")
        print()
        if Dstruct == '1':
            lst = LinkedList() #type bind lst as the custom Linked List class that i made
            isLinked = True
            break
        elif Dstruct == '2':
            lst = [] #the python list is created (dynamic array), we type bind lst as a python list
            isLinked = False
            break
        else:
            print("Invalid Choice, select 1 or 2!")

    runMenu(lst, isLinked)
"""
when this program runs, it will call the main function, which displais a 
small menu, which then calls the main menu (runMenu). Uses a while loop, if, 
else, else if (elif) statements.
"""
if __name__ == "__main__":
    main()

