from p41 import create_chunks

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    sents = create_chunks(lines)
    outputs = []
    for s in sents:
        for i in range(len(s)):
            if not any(m.pos == "名詞" for m in s[i].morphs):
                continue
            x_path = [i]
            dst = s[i].dst
            while dst != -1:
                x_path.append(dst)
                dst = s[dst].dst

            for j in range(i+1, len(s)):
                if not any(m.pos == "名詞" for m in s[j].morphs):
                    continue

                y_path = [j]
                y_dst = s[j].dst
                while dst != -1:
                    x_path.append(dst)
                    dst = s[dst].dst

                for k in x_path:
                    if k == j:
                        outputs.append(' -> '.join([s[k] for k in x_path]))
