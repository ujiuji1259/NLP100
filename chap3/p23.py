import re
if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    lines = [line for line in lines if re.match('=+.*?=+', line)]
    lines = [(line.replace('=', ''), line.count('=')//2) for line in lines]
    print(lines)
