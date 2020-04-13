import re
from p25 import get_template

def remove_stress(text):
    return re.sub("'+(.+?)'+", r'\1', text)

if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    dic = get_template(lines, "基礎情報")
    for k in dic.keys():
        orig = dic[k]
        dic[k] = remove_stress(dic[k])
    print(dic)
