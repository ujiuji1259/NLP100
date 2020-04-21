from p41 import create_chunks

def isPos(chunk, pos='名詞'):
    res = False
    for m in chunk.morphs:
        res = res or (m.pos == pos)

    return res


if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    sents = create_chunks(lines)
    for s in sents:
        for c in s:
            if c.dst != -1 and isPos(c, '名詞') and isPos(s[c.dst], '動詞'):
                print(str(c) + '\t' + str(s[c.dst]))
