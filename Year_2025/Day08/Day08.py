import math

from Day08.Circuit import Circuit
from Day08.Position import Position
from DayTemplate import Day


class Day08(Day):
    def __init__(self):
        test = False
        super().__init__(test=test)

        self.boxes = [Position(box) for box in self.data]
        self.connections = []
        self.connections = sorted(self.distance_of_two_distinct_boxes_map().items())
        self.connections = [(b1, b2) for _, (b1, b2) in self.connections]

    def distance_of_two_distinct_boxes_map(self):
        distance_to_boxes = {}
        for box_id, box in enumerate(self.boxes):
            for other_box_id, other_box in enumerate(self.boxes):
                if box_id >= other_box_id:
                    continue

                distance = box.distance(other_box)

                if distance in distance_to_boxes:
                    raise "shit double entry"

                distance_to_boxes[distance] = (box_id, other_box_id)

        return distance_to_boxes

    def circuits_from_connections(self, n_to_connect):
        circuits = []
        relevant_connections = self.connections[:n_to_connect]
        seen = set()
        for b1, b2 in relevant_connections:
            network = set()
            frontier = [b1, b2]
            while frontier:
                current = frontier.pop()
                if current in seen:
                    continue

                seen.add(current)
                network.add(current)

                for o1, o2 in relevant_connections:
                    if o1 == current or o2 == current:
                        frontier.append(o1 if o1 != current else o2)

            circuits.append(Circuit(list(network)))

        return circuits

    def circuits_from_connecting_n_closest(self, n_to_connect):
        circuits = self.circuits_from_connections(n_to_connect)

        return sorted(circuits, key=lambda b: b.size(), reverse=True)

    def get_last_connection_needed_for_complete_network(self):
        seen = set()
        connection_id = -1
        while len(seen) < 1000:
            connection_id += 1
            seen.add(self.connections[connection_id][0])
            seen.add(self.connections[connection_id][1])

        return connection_id

    def part1(self) -> str:
        return str(
            math.prod([circuit.size() for circuit in self.circuits_from_connecting_n_closest(1000)[:3]]))

    def part2(self) -> str:
        connection_id = self.get_last_connection_needed_for_complete_network()
        return str(self.boxes[self.connections[connection_id][0]].x * self.boxes[self.connections[connection_id][1]].x)
