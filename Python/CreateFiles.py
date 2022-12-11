class CreateFiles:

    # Nicht aus main.py aufrufen!!!
    @staticmethod
    def modify_main(start, end):
        main = open("main.py", "w")
        for x in range(start, end):
            main.write(f"import Day{x}\n")
        main.write("\nif __name__ == \"__main__\":")
        for x in range(start, end):
            main.write(f"\n    day{x} = Day{x}.Day{x}()")

    @staticmethod
    def create_files(start, end):
        for x in range(start, end + 1):
            data = open(f"Day{x}.py", "w")
            data.write(f'''class Day{x}:
        
                def __init__(self):
                    print("Day {x} Part 1: " + self.solve_first_puzzle())
                    print("Day {x} Part 2: " + self.solve_second_puzzle())
        
                def solve_first_puzzle(self) -> str:
                    input_data = open("Day{x}_input.txt", "r")
                    for line in input_data:
                        line = line.removesuffix("\\n")
        
                    return ""
        
                def solve_second_puzzle(self) -> str:
                    input_data = open("Day{x}_input.txt", "r")
                    for line in input_data:
                        line = line.removesuffix("\\n")
        
                    return ""
            ''')
            open(f"Day{x}_input.txt", "w")


CreateFiles.modify_main(1, 26)
