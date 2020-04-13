import re
if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    for line in lines:
        itr = re.search('\[\[ファイル:(.*?)\]\]', line)
        if itr:
            print(itr.groups()[0].split('|')[0].replace(' ', '_'))
