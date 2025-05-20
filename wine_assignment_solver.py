# wine_assignment_solver.py

import sys
from collections import defaultdict

def parse_tsv(file_path):
    """
    Parses a TSV file and returns a mapping of person_id to a list of wine_ids they like.
    Parameters:
        file_path (str): Path to the TSV input file.
    Returns:
        dict: Mapping of person_id to list of wine_ids.
    """
    person_to_wines = defaultdict(list)
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    person, wine = parts
                    person_to_wines[person].append(wine)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error while reading file: {e}")
        sys.exit(1)

    return person_to_wines

def assign_wines(person_to_wines):
    """
    Assigns wines to people based on their preferences, adhering to the constraints:
    - Each wine is given to at most one person.
    - Each person can receive up to 3 wines.

    Parameters:
        person_to_wines (dict): Mapping of person_id to list of wine_ids.

    Returns:
        dict: Mapping of person_id to list of assigned wine_ids.
    """
    assigned_wines = set()  # Tracks wines that have been assigned
    person_wine_map = defaultdict(list)  # Tracks wine assignments per person

    for person, wine_list in person_to_wines.items():
        for wine in wine_list:
            # Assign wine only if it's unassigned and person has less than 3 wines
            if wine not in assigned_wines and len(person_wine_map[person]) < 3:
                assigned_wines.add(wine)
                person_wine_map[person].append(wine)

    return person_wine_map

def write_output(assignments):
    """
    Prints the total number of assignments and each (person, wine) pair to stdout.

    Parameters:
        assignments (dict): Final mapping of person_id to their assigned wine_ids.
    """
    total = sum(len(wines) for wines in assignments.values())
    print(total)
    for person, wines in assignments.items():
        for wine in wines:
            print(f"{person}\t{wine}")

def main():
    """
    Main function to handle input arguments and orchestrate the workflow.
    Usage: python wine_assignment_solver.py <input_file.tsv>
    """
    if len(sys.argv) != 2:
        print("Usage: python wine_assignment_solver.py <input_file.tsv>")
        sys.exit(1)

    file_path = sys.argv[1]
    person_to_wines = parse_tsv(file_path)
    assignments = assign_wines(person_to_wines)
    write_output(assignments)

if __name__ == "__main__":
    main()
