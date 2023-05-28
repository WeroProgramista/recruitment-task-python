import sys
from collections import defaultdict
import re

BRICK_CODE_REGEX = re.compile("^[A-N]{4}$", re.IGNORECASE)


class BricksUsed:
    def __init__(self):
        self.stage_1 = 0
        self.stage_2 = 0


class Instructions:
    def __init__(self):
        self.stage1 = defaultdict(list)
        self.stage2 = defaultdict(list)

    def add_instruction(self, stage, number, brick_code):
        if stage == "stage1":
            self.stage1[number].append(brick_code)
        else:
            self.stage2[number].append(brick_code)

    def get_all_instructions(self, stage):
        return self.stage1 if stage == "stage1" else self.stage2

    def get_instruction(self, stage, instruction):
        return self.get_all_instructions(stage)[instruction]


class ConstructionProject:
    def __init__(self):
        self.box = defaultdict(int)
        self.total_missing = 0
        self.completed_buildings = 0
        self.incomplete_buildings = 0
        self.bricks_used = BricksUsed()
        self.instructions = Instructions()

    def construct(self):
        self.construct_building("stage1")
        self.construct_building("stage2")

    def construct_building(self, stage):
        for instruction in sorted(self.instructions.get_all_instructions(stage).keys()):
            bricks_needed = defaultdict(int)
            for brick in self.instructions.get_instruction(stage, instruction):
                bricks_needed[brick] += 1

            missing_bricks = self.calculate_missing_bricks(bricks_needed)
            self.total_missing += missing_bricks

            if missing_bricks == 0:
                self.process_successful_construction(stage, instruction)
            else:
                self.incomplete_buildings += 1

    def calculate_missing_bricks(self, bricks_needed):
        return sum(
            max(0, bricks_needed[brick] - self.box.get(brick, 0))
            for brick in bricks_needed
        )

    def process_successful_construction(self, stage, instruction):
        self.remove_used_bricks_from_box(stage, instruction)
        self.completed_buildings += 1
        if stage == "stage1":
            self.bricks_used.stage_1 += len(
                self.instructions.get_instruction(stage, instruction)
            )
        else:
            self.bricks_used.stage_2 += len(
                self.instructions.get_instruction(stage, instruction)
            )

    def remove_used_bricks_from_box(self, stage, instruction):
        for brick in self.instructions.get_instruction(stage, instruction):
            self.box[brick] -= 1

    def print_res(self):
        results = [
            str(self.bricks_used.stage_1),
            str(self.bricks_used.stage_2),
            str(sum(self.box.values())),
            str(self.total_missing),
            str(self.completed_buildings),
            str(self.incomplete_buildings),
        ]
        print("\n".join(results))


def validate(line, instruction_counters):
    if not line or line.strip() == "": # Ignoruje puste linie
        return None

    try:
        num, brick_code = line.strip().split(":")  # Dzieli i przypisuje do zmiennych
        if brick_code.endswith(";"):
            brick_code = brick_code.rstrip(";")  # Jeżeli jest ; jako znak konca lini to go usuwa
        else:
            rest = brick_code[4:]
            if rest.strip() != "":  # Jezeli cokolwiek innego wystepuje po kodzie klocka to klops
                klops()
    except ValueError:
        klops()

    # Sprawdza czy liczba jest to liczba naturalna oraz czy nie zawiera + i -, bo inaczej np. -0 przechodziło
    if not num.isdigit() or "-" in num or "+" in num: 
        klops()

    # Jezli nie mozna skonwertowac na inta to klops
    num = int(num) 
    if num < 0:
        klops()

    # O moze wystepowac tylko i wylacznie w boxie, a w instrukcjach juz nie
    if num == 0 and "O" in brick_code:
        pass
    
    # Sprawdza precompiled regex ktory jest na gorze (dokladnie 4 duze litery od A do N )
    elif BRICK_CODE_REGEX.match(brick_code) is None: 
        klops()

    # Dotatkowe sprawdzenie wielkich liter, poniewaz przy wielu testach regex czasem przepuszczal male litery
    if brick_code != brick_code.upper(): 
        klops()

    # Sprawdza czy ilosc klockow w pudelku nie przekracza 10 milonow
    if instruction_counters["total_bricks_in_box"] > 10000000: 
        klops()

    # Sprawdza czy ilosc instrukcji nie przekracza 1000 - pod uwage wzialem ze nie ma znaczenia kolejnosc
    # Nie moze byc wiecej niz 1000 roznych numerow instrukcji
    elif instruction_counters["total_instructions"] > 1000: 
        klops()

    # Sprawdza czy liczba jednej instrukcji nie powtarza sie wiecej niz 5000 razy
    # Ten sam numer instrukcji nie moze byc wiecej niz 5000 razy
    elif instruction_counters[num] > 5000: 
        klops()

    return num, brick_code


def klops():
    print("klops")
    exit(0)


def process_input(construction_project):
    instruction_counters = defaultdict(int)
    for line in sys.stdin:
        validated_data = validate(line, instruction_counters)
        if validated_data is not None:
            num, brick_code = validated_data
            if num == 0:
                construction_project.box[brick_code] += 1
            else:
                stage = "stage1" if num % 3 == 0 else "stage2"
                construction_project.instructions.add_instruction(
                    stage, num, brick_code
                )


if __name__ == "__main__":
    construction_project = ConstructionProject()
    process_input(construction_project)
    construction_project.construct()
    construction_project.print_res()