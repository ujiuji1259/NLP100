# mecab neko.txt > neko.txt.mecab
from p30 import load_mecab_output
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib

if __name__ == '__main__':
    lines = load_mecab_output('neko.txt.mecab')
    cat_co = []
    for line in lines:
        for i in range(len(line)):
            if line[i]['surface'] == '猫':
                if i == 0:
                    cat_co.append(line[i+1]['surface'])
                elif i == len(line) - 1:
                    cat_co.append(line[i-1]['surface'])
                else:
                    cat_co.append(line[i+1]['surface'])
                    cat_co.append(line[i-1]['surface'])


    counter = collections.Counter(cat_co).most_common()[:10]
    word = [c[0] for c in counter]
    freq = [c[1] for c in counter]
    plt.bar(word, freq)
    plt.show()

