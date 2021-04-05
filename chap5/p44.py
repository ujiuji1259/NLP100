from p41 import create_chunks
import pydot

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        lines = [line.split('\n') for line in f.read().split('EOS\n') if line != '']

    lines = [[l.replace('\t', ',').split(',') for l in line if l != ''] for line in lines]

    edges = []
    sents = create_chunks(lines)
    for c in sents[10]:
        if c.dst != -1:
            edges.append((str(c), str(sents[10][c.dst])))

    g = pydot.graph_from_edges(edges,directed=True)
    g.set_rankdir('LR')
    g.write_png("dependenttre.png")
