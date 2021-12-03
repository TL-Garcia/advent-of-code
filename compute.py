import sys
import re
from utils import get_list_from_file

is_terminal_script = __name__ == '__main__'


if is_terminal_script:
    script_path = sys.argv[1]
    input_path = script_path + '/input.txt'

    #adds the folder containing the main logic to the path
    sys.path.insert(0, script_path)

    lines = get_list_from_file(input_path)

    from main import main
    print(main(lines))
elif not is_terminal_script:
    print('Cannot call compute as a module')
