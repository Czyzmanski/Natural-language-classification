import os


def get_class_name(path):
    start = len(path)
    try:
        start -= path[::-1].index('/')
    except ValueError:
        start = 0
    return path[start:]


def get_observation(path, class_name):
    freq = [0 for i in range(65, 91)]
    with open(path) as f:
        for line in f:
            for c in line:
                freq[ord(c) - 65] += 1
    total = sum(freq)
    for i in range(len(freq)):
        freq[i] = freq[i] / total
    freq.append(class_name)
    return freq


def prepare_data(src_path, src):
    data = []
    for directory in src:
        for file in os.listdir('/'.join([src_path, directory])):
            path = '/'.join([src_path, directory, file])
            class_name = get_class_name(directory)
            data.append(get_observation(path, class_name))
    return data


def filter_input(input):
    return ''.join([c for c in input.upper() if 65 <= ord(c) <= 90])


def get_observation_input(input):
    freq = [0 for i in range(65, 91)]
    for c in input:
        freq[ord(c) - 65] += 1
    total = sum(freq)
    for i in range(len(freq)):
        freq[i] = freq[i] / total
    return freq
