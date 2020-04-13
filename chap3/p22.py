import re
if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    lines = [line[11:-2].split('|')[0] for line in lines if line[:10] == '[[Category']
    print(lines)
