import os

from solution.kmp import kmp_search
from utils.file_utils import read_from_file, write_to_file


def main(filename):
    os.chdir('../files/in')
    input_data = read_from_file(filename)
    string = input_data[0]
    substring = input_data[1]
    if not string or not substring or len(substring) > len(string):
        os.chdir('../')
        raise SystemExit(1)
    result = kmp_search(string, substring)
    os.chdir('../out')
    write_to_file(filename, result)
    os.chdir('../')
    return result
