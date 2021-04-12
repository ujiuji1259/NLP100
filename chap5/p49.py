from p41 import create_chunks
import re

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    sents = create_chunks(lines)
    outputs = []
    for s in sents:
        noun_idxs = [i for i, c in enumerate(s) if any([m.pos == "名詞" for m in c.morphs])]
        for i in range(len(noun_idxs)):
            for j in range(i+1, len(noun_idxs)):
                x_idx = noun_idxs[i]
                y_idx = noun_idxs[j]
                path_x = []
                path_y = []
                while x_idx != y_idx:
                    if x_idx < y_idx:
                        path_x.append(x_idx)
                        x_idx = s[x_idx].dst
                    else:
                        path_y.append(y_idx)
                        y_idx = s[y_idx].dst

                if len(path_x) == 0 or len(path_y) == 0:
                    path = path_x if len(path_x) != 0 else path_y
                    X = ''.join([m.surface if m.pos != '名詞' else "X" for m in s[path[0]].morphs])
                    Y = ''.join([m.surface if m.pos != '名詞' else "Y" for m in s[x_idx].morphs])
                    X = re.sub("X+", "X", X)
                    Y = re.sub("Y+", "Y", Y)
                    mid = [str(s[c]) for c in path[1:]]
                    outputs.append(X + ' -> ' + ' -> '.join(mid) + ' -> ' + Y)
                else:
                    X = ''.join([m.surface if m.pos != '名詞' else "X" for m in s[path_x[0]].morphs])
                    X = re.sub("X+", "X", X)
                    X = [X] + [str(s[c]) for c in path_x[1:]]

                    Y = ''.join([m.surface if m.pos != '名詞' else "Y" for m in s[path_y[0]].morphs])
                    Y = re.sub("Y+", "Y", Y)
                    Y = [Y] + [str(s[c]) for c in path_y[1:]]

                    output = [" -> ".join(X), ''.join(Y), str(s[x_idx])]
                    outputs.append(" | ".join(output))
print(outputs)
