import re
from p25 import get_template
from p26 import remove_stress

def get_link(text):
    word = re.search('(.*?)\[\[(.*?)\]\](.*?)', text)
    if word is not None and word.groups()[1][:4] not in ['ファイル', 'http', 'Cate']:
        link_word = word.groups()[1].split('|')[-1]
        print(word, link_word)
        return word.groups()[0] + link_word + word.groups()[2]
    return text

if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    dic = get_template(lines, "基礎情報")
    for k in dic.keys():
        orig = dic[k]
        dic[k] = remove_stress(dic[k])
        dic[k] = get_link(dic[k])

