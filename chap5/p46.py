from p41 import create_chunks

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    sents = create_chunks(lines)
    outputs = []
    for s in sents:
        for c in s:
            verb = [(morph, c.dst) for morph, src in zip(c.morphs, c.srcs) if morph.pos == "動詞"]
            if len(verb) == 0:
                continue
            dst_chunk = s[verb[0][1]]
            pos = [(morph.surface, str(dst_chunk)) for morph in dst_chunk.morphs if morph.pos == "助詞"]
            if len(pos) == 0:
                continue

            sort_pos = sorted(pos, key=lambda x: x[0])

            outputs.append(' '.join([verb[0][0].base] + [p[0] for p in sort_pos] + [p[1] for p in sort_pos]))
    print('\n'.join(outputs))