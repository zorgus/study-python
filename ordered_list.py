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

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass

    def isEmpty(self):
        pass

    def size(self):
        pass

    def index(self, item):
        pass

    def pop(self):
        pass

    def pop(self, pos):
        pass
