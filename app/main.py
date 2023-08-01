from loguru import logger

from app.models.rover import Rover


def process_input(input_file):
    """
    Processes the input file and extracts the plateau dimensions and rover 
    data.

    Parameters:
        input_file (str): The path to the input file.

    Returns:
        tuple: A tuple containing the plateau dimensions (plateau_x, plateau_y) 
        and a list of rovers.
               Each rover is represented as a tuple containing the rover 
               object and its instructions.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    plateau_x, plateau_y = map(int, lines[0].split())
    rovers_data = lines[1:]

    rovers = []
    for i in range(0, len(rovers_data), 2):
        x, y, direction = rovers_data[i].split()
        instructions = rovers_data[i + 1].strip()
        rover = Rover(int(x), int(y), direction)
        rovers.append((rover, instructions))

    return plateau_x, plateau_y, rovers

    
def run_rovers(plateau_x, plateau_y, rovers):
    """
    Run the rovers on the plateau.

    Parameters:
        plateau_x (int): The x-coordinate of the plateau.
        plateau_y (int): The y-coordinate of the plateau.
        rovers (List[Tuple[Rover, List[str]]]): A list of tuples containing 
        the rover object and its instructions.

    Returns:
        List[Tuple[int, int, str]]: A list of tuples containing the final 
        x-coordinate, y-coordinate, and direction of each rover after 
        executing the instructions.
    """
    for rover, instructions in rovers:
        rover.run(instructions, plateau_x, plateau_y)

    return [(rover.x, rover.y, rover.direction) for rover, _ in rovers]


def write_output(output_file, results):
    """
    Writes the results to an output file.

    Parameters:
        output_file (str): The path to the output file.
        results (list): A list of tuples containing the results.

    Returns:
        None
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            x, y, direction = result
            file.write(f"{x} {y} {direction}\n")
            
            
if __name__ == "__main__":
    # TODO: Create logic for manual data input
    input_file = "tests/static/input.txt"
    output_file = "tests/static/output.txt"

    plateau_x, plateau_y, rovers = process_input(input_file)
    results = run_rovers(plateau_x, plateau_y, rovers)
    write_output(output_file, results)

    for result in results:
        print(f"{result[0]} {result[1]} {result[2]}")
