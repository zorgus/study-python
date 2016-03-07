class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.rear = None

    def __repr__(self):
        string = "["
        current = self.head
        while current != None:
            string += str(current.getData())
            if current.getNext() != None:
                string += ","
            current = current.getNext()
        string += "]"
        return string

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.rear == None:
            self.rear = temp
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if current.getNext() == None:
            self.rear = previous
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.rear = temp
        else:
            self.rear.setNext(temp)
            self.rear = temp

    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count += 1
        if found:
            return count
        else:
            return -1

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        while current != None and count != pos:
            count += 1
            previous = current
            current = current.getNext()
        temp = Node(item)
        if previous == None:
            self.head = temp
            self.rear = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)

mylist = UnorderedList()
mylist.insert(1, 22)
print mylist
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.append(46)
mylist.insert(3, 23)
print mylist

print(mylist.size())
print(mylist.search(93))
print(mylist.index(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())
mylist.append(41)
mylist.remove(54)
print(mylist.size())
mylist.remove(93)
mylist.remove(41)
print mylist
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
mylist.remove(46)
print mylist
