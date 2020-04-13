# python p16.py popular-names.txt 10
# split -l 10 popular-names.txt
import sys

def file_split(fn, n):
    with open(fn, 'r') as f:
        lines = [line.replace("\n", '') for line in f.readlines()]

    return ['\n'.join(lines[i:i+n]) for i in range(0, len(lines), n)]

if __name__ == "__main__":
    fn, n = sys.argv[1], int(sys.argv[2])
    print('\n\n'.join(file_split(fn, n)))

