
from p41 import create_chunks

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    sents = create_chunks(lines)
    outputs = []
    for s in sents:
        for c in s:
            nouns = [(c, c.dst) for morph in c.morphs if morph.pos == "名詞"]
            if len(nouns) == 0:
                continue
            nouns = nouns[0]
            dst = nouns[1]
            path = [str(c)]
            while dst != -1:
                path.append(str(s[dst]))
                dst = s[dst].dst
            outputs.append(' -> '.join(path))


    print('\n'.join(outputs))
