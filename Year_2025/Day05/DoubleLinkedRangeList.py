class DoubleLinkedRangeList:
    class Node:
        def __init__(self, min, max):
            self.min = min
            self.max = max
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_in(self, value):
        current = self.head
        while current is not None:
            if current.min <= value <= current.max:
                return True
            current = current.next

        return False

    def get_in_length(self):
        current = self.head
        in_length = 0
        while current is not None:
            in_length += current.max - current.min + 1
            current = current.next

        return in_length

    def append(self, min, max):
        if self.tail is None:
            self.head = self.Node(min, max)
            self.tail = self.head
            self.length = 1
            return

        new = self.Node(min, max)
        new.prev = self.tail
        self.tail.next = new
        self.tail = new
        self.length += 1

    def insert(self, min, max):
        current = self.head
        while current is not None and min > current.max+1:
            current = current.next

        if current is None:
            self.append(min, max)
            return

        # min out of current
        if min < current.min:
            # max out of current -> new prev
            if max < current.min - 1:
                new = self.Node(min, max)
                new.next = current
                self.length += 1

                if current == self.head:
                    current.prev = new
                    self.head = new
                    return

                new.prev = current.prev
                current.prev.next = new
                current.prev = new
                return

            # max within -> new min
            if max <= current.max:
                current.min = min
                return

            # current within new
            if max > current.max:
                # last item -> new minmax
                if self.length == 1 or current == self.tail:
                    current.min = min
                    current.max = max
                    return

                # first item -> delete current
                if current == self.head:
                    current.next.prev = None
                    self.head = current.next

                else: # any item -> delete current
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.length -= 1
                self.insert(min, max)

        # min within current
        elif min >= current.min:
            # if new completely in current -> ignore new
            if max <= current.max:
                return

            # max doesnt touch next -> new max
            if current == self.tail or max < current.next.min - 1:
                current.max = max
                return

            # max touches next
            # first item
            if current == self.head:
                current.next.prev = None
                self.head = current.next

            else: # any item
                current.prev.next = current.next
                current.next.prev = current.prev

            self.length -= 1
            self.insert(current.min, max)
