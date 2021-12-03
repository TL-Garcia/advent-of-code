def get_list_from_file(file_path):
    with open(file_path) as file:
        return file.read().splitlines()

