from pathlib import Path

def read_file(day, type):
    current_abs_path = Path(__file__).parent
    filename = f'day{day}_input_{type}.txt'

    with open(Path(current_abs_path, filename)) as f:
        content = f.read()
    return content
