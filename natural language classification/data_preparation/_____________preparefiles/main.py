import os
import shutil


def filter_out(line):
    return ''.join([c for c in line.upper() if 65 <= ord(c) <= 90])


def split_file(path):
    with open(path, encoding='utf-8', errors='ignore') as f:
        return [filter_out(line.strip()) for line in f]


def create_files(dir_name, lines):
    i, n = 0, 1
    while i < len(lines):
        j = 0
        with open(dir_name + '/' + str(n) + '.txt', 'w') as f:
            while i + j < len(lines) and j < 100:
                f.write(lines[i + j])
                j += 1
        i += j
        n += 1


with os.scandir('..') as entries:
    for entry in entries:
        if entry.is_file():
            lines = split_file(entry.path)
            dir_name = '../' + entry.name[:-4]
            if os.path.isdir(dir_name):
                shutil.rmtree(dir_name)
            os.mkdir(dir_name)
            create_files(dir_name, lines)
