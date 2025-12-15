class Device:
    def __init__(self, name: str):
        self.name = name
        self.outputs = []
        self.inputs = []

    def __repr__(self):
        return self.name