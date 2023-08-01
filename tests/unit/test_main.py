from app.main import process_input, run_rovers, write_output
from app.models.rover import Rover


def test_process_input():
    """
    Test the process_input() function.

    This function tests whether the process_input() function correctly 
    processes the input file and returns the expected values.

    Parameters:
        None

    Returns:
        None
    """
    input_file = "tests/static/input.txt"
    plateau_x, plateau_y, rovers = process_input(input_file)
    assert plateau_x == 5
    assert plateau_y == 5
    assert len(rovers) == 2

def test_run_rovers():
    """
    Run the rovers on the given plateau.

    Parameters:
    - plateau_x (int): The x-coordinate of the plateau.
    - plateau_y (int): The y-coordinate of the plateau.
    - rovers (list): A list of tuples containing the initial position and 
    instructions for each rover.

    Returns:
    - list: A list of tuples containing the final position and orientation of 
    each rover.
    """
    plateau_x, plateau_y, rovers = 5, 5, [(Rover(1, 2, 'N'), 'LMLMLMLMM'),
                                          (Rover(3, 3, 'E'), 'MMRMMRMRRM')]
    results = run_rovers(plateau_x, plateau_y, rovers)
    assert results == [(1, 3, 'N'), (5, 1, 'E')]

def test_write_output(tmp_path):
    """
    Generates the function comment for the given function body.
    
    Args:
        tmp_path (str): The path to the temporary directory.
        
    Returns:
        None
    """
    output_file = tmp_path / "output.txt"
    results = [(1, 3, 'N'), (5, 1, 'E')]
    write_output(output_file, results)
    
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    assert content.strip() == "1 3 N\n5 1 E"
