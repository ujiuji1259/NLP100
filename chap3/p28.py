import re
from p25 import get_template
from p26 import remove_stress
from p27 import get_link

def remove_markup(text):
    text = re.sub(r'<ref .*?\s?/?>', '', text)
    text = re.sub(r'<ref>.*?$', '', text)
    text = re.sub(r'<reference/>', '', text)
    word = re.search('(.*?)(\{\{|\[\[)(.*?)(\]\]|\}\})(.*?)', text)
    if word is not None:
        text = word.groups()[0] + word.groups()[2].split('|')[-1] + word.groups()[4]
    return text

if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    dic = get_template(lines, "基礎情報")
    for k in dic.keys():
        orig = dic[k]
        dic[k] = remove_stress(dic[k])
        dic[k] = get_link(dic[k])
        dic[k] = remove_markup(dic[k])

    print(dic)
