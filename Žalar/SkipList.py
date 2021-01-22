import random
import time


class Node:
    def __init__(self, height=0, data=None):
        self.data = data
        self.next = [None] * (height + 1)


class SkipList:

    def __init__(self, maxHeight=100, chance=0.5):
        self.maxHeight = maxHeight
        self.head = Node(height=self.maxHeight)
        self.len = 0
        self.minHeight = 0
        self.chance = chance
        self.listHeight = 0

    def __len__(self):
        return self.len

    def find(self, data):
        temp = self.head
        for i in range(self.listHeight, -1, -1):
            while temp.next[i] and temp.next[i].data < data:
                temp = temp.next[i]
            if temp.next[i] and temp.next[i].data == data:
                return True

        return False

    def randomHeight(self):
        height = self.minHeight
        while random.uniform(0, 1) < self.chance and height < self.maxHeight:
            height += 1
        return height

    def remove(self, data):
        temp = self.head
        update = [None] * (self.maxHeight + 1)
        for i in range(self.listHeight, -1, -1):
            while temp.next[i] and temp.next[i].data < data:
                temp = temp.next[i]
            update[i] = temp

        temp = temp.next[self.minHeight]
        if temp is None or temp.data == data:
            for i in range(0, self.listHeight+1):
                if update[i] and update[i].next[i] != temp:
                    break
                update[i].next[i] = temp.next[i]
        self.len -=1



    def insert(self, data):
        temp = self.head
        update = [None] * (self.maxHeight+1)
        for i in range(self.listHeight, -1, -1):
            while temp.next[i] and temp.next[i].data < data:
                temp = temp.next[i]
            update[i] = temp

        temp = temp.next[self.minHeight]
        if temp is None or temp.data != data:
            height = self.randomHeight()
            if height > self.listHeight:
                for i in range(height,-1,-1):
                    if update[i]:
                        pass
                    else:
                        update[i] = self.head
                self.listHeight = height

            temp = Node(height, data)
            for i in range(self.minHeight, height + 1):
                if update[i]:
                    temp.next[i] = update[i].next[i]
                    update[i].next[i] = temp
            self.len +=1

    def printList(self):
        temp = self.head.next[self.minHeight]
        print("{", end="")
        while temp:
            print(temp.data, end="")
            temp = temp.next[self.minHeight]
            if temp:
                print(",", end="")
        print("}")



if __name__ == '__main__':
    l = SkipList(100,0.5)
    l.insert(5)
    l.printList()
    l.insert(10)
    l.printList()
    l.insert(7)
    l.printList()
    l.insert(8)
    l.printList()
    l.insert(6)
    l.printList()
    #print(len(l))
    l.remove(5)
    #print(len(l))
    l.printList()
    print(f"is 7 in the list ? {l.find(7)}")
    l.remove(7)
    l.printList()
    print(f"is 7 in the list ? {l.find(7)}")
