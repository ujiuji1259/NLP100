# python p17.py popular-names.txt
# cut -f 1 popular-names.txt | sort | uniq | tr '\n' ','
import sys

if __name__ == "__main__":
    fn = sys.argv[1]
    with open(fn, 'r') as f:
        lines = [line.split('\t')[0] for line in f.read().split('\n') if line != '']

    print(set(lines))
