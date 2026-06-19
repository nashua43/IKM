class Node:
    """Узел односвязного списка."""

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        """Проверка на пустоту."""
        return self.head is None

    def enqueue(self, item):
        """Добавление элемента в конец очереди."""
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Удаление и возврат первого элемента."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return data

    def peek(self):
        """Возврат первого элемента без удаления."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.head.data

    def size(self):
        """Текущий размер очереди."""
        return self._size