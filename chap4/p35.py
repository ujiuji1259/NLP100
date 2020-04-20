# mecab neko.txt > neko.txt.mecab
from p30 import load_mecab_output
import collections

if __name__ == '__main__':
    lines = load_mecab_output('neko.txt.mecab')
    lines = [l['surface'] for line in lines for l in line]
    counter = collections.Counter(lines)
    print(counter.most_common())

