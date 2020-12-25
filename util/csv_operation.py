import csv


def read_csv(path):
    with open(path, 'r') as f:
        t = csv.reader(f)
        result = []
        for i in t:
            result.append(i)
        result.pop(0)
    return result


if __name__ == '__main__':
    read_csv('../sr.csv')
