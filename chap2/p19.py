# python p19.py popular-names.txt
# cut -f 1 popular-names.txt | sort | uniq -c | sort -k 1 -n -r | rev | cut -f 1 -d ' ' | rev | tr '\n' ','
import sys
import collections

if __name__ == "__main__":
    fn = sys.argv[1]
    with open(fn, 'r') as f:
        words = [line.split('\t')[0] for line in f.read().split("\n") if line != '']

    counter = collections.Counter(words)
    print([c[0] for c in counter.most_common()])


