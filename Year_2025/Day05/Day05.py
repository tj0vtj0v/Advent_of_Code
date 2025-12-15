from Day05.DoubleLinkedRangeList import DoubleLinkedRangeList
from DayTemplate import Day


class Day05(Day):
    def __init__(self):
        super().__init__()

        fresh_ranges, self.item_ids = self.data.get_items_from_input()

        self.ordered_ranges = DoubleLinkedRangeList()
        for fresh_range in fresh_ranges:
            self.ordered_ranges.insert(*[int(m) for m in fresh_range.split("-")])

    def part1(self) -> str:
        counter = 0
        for item_id in self.item_ids:
            counter += self.ordered_ranges.is_in(int(item_id))

        return str(counter)

    def part2(self) -> str:
        return str(self.ordered_ranges.get_in_length())