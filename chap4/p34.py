# mecab neko.txt > neko.txt.mecab
from p30 import load_mecab_output

if __name__ == '__main__':
    lines = load_mecab_output('neko.txt.mecab')
    nouns = set()
    for l in lines:
        idx = 0
        while idx < len(l):
            while idx < len(l) and l[idx]['pos'] != '名詞':
                idx += 1
            noun = []
            while idx < len(l) and l[idx]['pos'] == '名詞':
                noun.append(l[idx]['surface'])
                idx += 1
            if noun:
                nouns.add(''.join(noun))

    print(nouns)

