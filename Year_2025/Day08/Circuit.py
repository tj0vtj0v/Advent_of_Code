class Circuit:
    def __init__(self, boxes: list[int] = []):
        self.boxes = boxes

    def size(self):
        return len(self.boxes)

    def add(self, box):
        self.boxes.append(box)

    def remove(self, box):
        self.boxes.remove(box)

    def __iter__(self):
        return iter(self.boxes.copy())

    def __repr__(self):
        return f"JunctionNetwork({self.boxes})"
