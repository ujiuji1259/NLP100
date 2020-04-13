# python p18.py popular-names.txt
# sort -k 3 -n -r popular-names.txt
import sys

if __name__ == "__main__":
    fn = sys.argv[1]
    with open(fn, 'r') as f:
        lines = [line.split('\t') for line in f.read().split("\n") if line != '']

    lines.sort(key=lambda s: int(s[2]), reverse=True)
    print('\n'.join(['\t'.join(line) for line in lines]))
