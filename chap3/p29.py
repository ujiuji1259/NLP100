import re
import requests
import json
from p25 import get_template
from p26 import remove_stress
from p27 import get_link
from p28 import remove_markup

def get_flag_image(text):
    url_base = 'https://commons.wikimedia.org/w/api.php?'
    url_prefix = 'action=query&titles=File:'
    url_file = text.replace(' ', '_')
    url_suffix = '&prop=imageinfo&iiprop=url&format=json'
    url = url_base + url_prefix + url_file + url_suffix

    data = requests.get(url)
    return re.search('"url":"(.*?)"', data.text).groups()[0]

if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    dic = get_template(lines, "基礎情報")
    for k in dic.keys():
        orig = dic[k]
        dic[k] = remove_stress(dic[k])
        dic[k] = get_link(dic[k])
        dic[k] = remove_markup(dic[k])
        if k == '国旗画像':
            print(get_flag_image(dic[k]))


