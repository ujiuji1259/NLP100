# mecab neko.txt > neko.txt.mecab
from p30 import load_mecab_output
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib

if __name__ == '__main__':
    lines = load_mecab_output('neko.txt.mecab')
    lines = [l['surface'] for line in lines for l in line]
    counter = collections.Counter(lines).most_common()
    freq = [c[1] for c in counter]
    rank = list(range(1, len(freq)+1))
    plt.plot(rank, freq)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

