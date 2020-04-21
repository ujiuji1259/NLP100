from p40 import Morph
from collections import defaultdict

class Chunk(object):
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]
    lines = [[Morph(l[0], l[7], l[1], l[2]) if l[0][0] != '*' else l[0].split() for l in line] for line in lines]

    sents = []
    for line in lines:
        sent = []
        chunk_idx = defaultdict(list)
        for l in line:
            if isinstance(l, list):
                idx_to = int(l[2][:-1])
                chunk_idx[idx_to].append(int(l[1]))
                idx_from = chunk_idx[int(l[1])]
                sent.append(Chunk([], idx_to, idx_from))
            else:
                sent[-1].morphs.append(l)
        sents.append(sent)

    for l in sents[7]:
        print([t.surface for t in l.morphs])
        print(l.dst)

