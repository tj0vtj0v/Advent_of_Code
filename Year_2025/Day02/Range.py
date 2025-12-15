class Range:
    def __init__(self, data: str):
        self.start, self.end = map(int, data.split("-"))

    def count_repeating_twice_ids(self) -> int:
        return sum([id for id in range(self.start, self.end + 1) if self.check_repeating_twice(id)])

    def check_repeating_twice(self, id: int) -> bool:
        if len(str(id)) % 2 != 0:
            return False

        for i in range(len(str(id)) // 2):
            if str(id)[i] != str(id)[len(str(id)) // 2 + i]:
                return False

        return True

    def count_repeating_ids(self) -> int:
        return sum([id for id in range(self.start, self.end + 1) if self.check_repeating(id)])

    def check_repeating(self, id: int) -> bool:
        id_length = len(str(id))
        for step in range(1, id_length // 2 + 1):
            if id_length % step != 0:
                continue

            valid = True
            for start in range(0, step):
                if len(set(str(id)[start::step])) != 1:
                    valid = False
                    break

            if valid:
                return True

        return False

