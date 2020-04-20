# mecab neko.txt > neko.txt.mecab
from p30 import load_mecab_output

if __name__ == '__main__':
    lines = load_mecab_output('neko.txt.mecab')
    noun = set()
    for l in lines:
        for i in range(1,len(l)-1):
            if l[i]['surface'] == 'の' and l[i-1]['pos'] == '名詞' and l[i+1]['pos'] == '名詞':
                noun.add(l[i-1]['surface'] + l[i]['surface'] + l[i+1]['surface'])
    print(noun)

