# Queue in Python

Queue

```sh
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
```

Print Queue

```sh
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
```

Enqueue

```sh
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
```

Dequeue

```sh
    def dequeue(self):
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
```

# Program Example
And this is a simple program that I made using Queue

![image](https://github.com/yogawanadityapratama/strudat-queue-program/assets/123430193/4f656dea-8202-4475-8f69-7a743cda28c8)
