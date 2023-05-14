import os

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def peek(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

beri = Queue(10000)
beri.enqueue(10001)
beri.enqueue(10002)
beri.enqueue(10003)
beri.enqueue(10004)
beri.enqueue(10005)
beri.enqueue(10006)
beri.enqueue(10007)
beri.enqueue(10008)
beri.enqueue(10009)
beri.enqueue(10010)

panggil = Queue(10000)
panggil.enqueue(10001)
panggil.enqueue(10002)
panggil.enqueue(10003)
panggil.enqueue(10004)
panggil.enqueue(10005)
panggil.enqueue(10006)
panggil.enqueue(10007)
panggil.enqueue(10008)
panggil.enqueue(10009)
panggil.enqueue(10010)

lis = Queue(10000)
lis.enqueue(10001)
lis.enqueue(10002)
lis.enqueue(10003)
lis.enqueue(10004)
lis.enqueue(10005)
lis.enqueue(10006)
lis.enqueue(10007)
lis.enqueue(10008)
lis.enqueue(10009)
lis.enqueue(10010)

def enqueue():
    print(beri.peek().value)

def peek():
    print(panggil.peek().value)

def list():
    lis.print_queue()

def showHeader():
    print(f"1. Beri Nasabah Nomer Antrian")
    print(f"2. Panggil Nasabah dari Yang Terlama")
    print(f"3. List Antrian")
    print(f"4. Exit")

def display():
    while(True):
        showHeader()
        user_option = input("Input Number: ")
        match user_option:
            case "1":
                enqueue()
            case "2":
                peek()
            case "3":
                list()
            case "4":
                break
    print("Program berakhir, Terimakasih")
display()