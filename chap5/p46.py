from p41 import create_chunks

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    sents = create_chunks(lines)
    outputs = []
    for s in sents:
        for c in s:
            verb = [(morph, c.srcs) for morph, src in zip(c.morphs, c.srcs) if morph.pos == "動詞"]
            if len(verb) == 0:
                continue
            verb = verb[0]
            poss = []
            for src in verb[1]:
                pos = [p.surface for p in s[src].morphs if p.pos == "助詞"]
                if not pos:
                    continue
                poss.append((pos[0], str(s[src])))
            poss = sorted(poss)
            if not poss:
                continue
            outputs.append(verb[0].base + ' ' + ' '.join([p[0] for p in poss]) + ' ' + ' '.join([p[1] for p in poss]))
    print('\n'.join(outputs))