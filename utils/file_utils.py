def read_from_file(filename):
    with open(filename + '.in', 'r') as file:
        return file.readline(), file.readline()


def write_to_file(filename, result):
    with open(filename + '.out', 'w') as file:
        file.write(str(result))
