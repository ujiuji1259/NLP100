# mecab neko.txt > neko.txt.mecab

def load_mecab_output(fn):
    with open(fn, 'r') as f:
        lines = [[l.replace('\t', ',').split(',') for l in line.split('\n') if l != ''] for line in f.read().split('EOS\n') if line != '']
    feature_list = ['surface', 'base', 'pos', 'pos1']
    lines = [[dict(zip(feature_list, [l[0], l[7], l[1], l[2]])) for l in line] for line in lines]
    return lines

if __name__ == '__main__':
    load_mecab_output('neko.txt.mecab')
