class Monkey:

    def __init__(self, starting_items: list, operation: str, test: int, monkey_true: int, monkey_false: int) -> None:
        self.__item_list = starting_items
        self.__operation = operation
        self.__test = test
        self.__inspections = 0
        self.__monkey_true = monkey_true
        self.__monkey_false = monkey_false

    def get_inspections(self) -> int:
        return self.__inspections

    def add_item(self, item: int) -> None:
        self.__item_list.append(item)

    def do_turn(self, monkeys: list) -> None:
        for item in self.__item_list:
            if self.calculate_next(item)[0]:
                monkeys[self.__monkey_true].add_item(self.calculate_next(item)[1])
            else:
                monkeys[self.__monkey_false].add_item(self.calculate_next(item)[1])
            self.__inspections += 1
        self.__item_list = []

    def calculate_next(self, item: int) -> list:
        old = item
        worry = eval(self.__operation[6:])
        # Für Part 2 deaktivieren:
        #worry = int(worry / 3)
        if worry % self.__test == 0:
            return [True, worry]
        else:
            return [False, worry]
