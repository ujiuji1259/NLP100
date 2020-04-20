# mecab neko.txt > neko.txt.mecab
from p30 import load_mecab_output

if __name__ == '__main__':
    lines = load_mecab_output('neko.txt.mecab')
    verb = {l['surface'] for line in lines for l in line if l['pos'] == '動詞'}
    print(verb)
