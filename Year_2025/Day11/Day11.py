from Day11.Device import Device
from DayTemplate import Day


class Day11(Day):
    def __init__(self):
        super().__init__(test=False)

        self.devices: dict[str, Device] = {"out": Device("out")}
        for device in self.data:
            new = Device(device.split(":")[0])
            self.devices[new.name] = new

        for line in self.data:
            device_name, outputs = line.split(":")
            for output in outputs.strip().split(" "):
                self.devices[device_name].outputs.append(self.devices[output])

    def get_paths_from_to(self, source_device: str, target_device: str, part_2: bool = False, killer: list[str] =[]):
        frontier = [(node, [source_device]) for node in self.devices[source_device].outputs]
        num_of_paths = 0
        while frontier:
            current, path = frontier.pop()

            if current.name == target_device:
                if not part_2 or ("fft" in path and "dac" in path):
                    num_of_paths += 1
                    continue

            if len(current.outputs) == 0 or current.name in path or current in killer:
                continue

            for output in current.outputs:
                frontier.append((output, path + [current]))

        return num_of_paths

    def get_all_outs(self, node: str):
        killer = []

        frontier = [node]
        while frontier:
            current = frontier.pop()
            if current in killer:
                continue

            killer.append(current)
            frontier.extend([o.name for o in self.devices[current].outputs])

        return killer

    def part1(self) -> str:
        return str(self.get_paths_from_to("you", "out"))

    def part2(self) -> str:
        paths = self.get_paths_from_to("svr", "fft", True, self.get_all_outs("fft"))
        return str(paths)
