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
            srcs = verb[1]
            poss = []
            base_predicate = ""
            for src in srcs:
                src_chunk = s[src]
                if (len(src_chunk.morphs) == 2
                and src_chunk.morphs[0].pos1 == "サ変接続"
                and src_chunk.morphs[1].surface == "を"):
                    base_predicate = "".join([src_chunk.morphs[0].surface, src_chunk.morphs[1].surface, verb[0].base])

                pos = [(m.surface, str(src_chunk)) for m in src_chunk.morphs if m.pos == "助詞"]
                if len(pos) != 0:
                    poss.append(pos[0])
            if base_predicate:
                if poss:
                    poss = sorted(poss)
                outputs.append(' '.join([base_predicate] + [p[0] for p in poss] + [p[1] for p in poss]))
    print('\n'.join(outputs))
