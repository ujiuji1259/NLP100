import re

def get_template(texts, template):
    idx = 0
    res = {}
    start_key = re.compile('\{\{'+template)
    end_key = re.compile('^\}\}$')
    field_key = re.compile('\|(.+)$')
    ref_start_key = re.compile('<ref>')
    ref_end_key = re.compile('</ref>')
    split_key = re.compile('\s+=\s*')

    template_flag = False
    while idx < len(texts):
        if template_flag:
            if end_key.search(texts[idx]):
                break
            p1 = field_key.search(texts[idx])
            p2 = ref_start_key.search(texts[idx])
            if p1 and not p2:
                field, value = split_key.split(p1.groups()[0])
            elif p1 and p2:
                field, value = split_key.split(p1.groups()[0])
                if not ref_end_key.search(texts[idx]):
                    idx += 1
                    while not ref_end_key.search(texts[idx]):
                        value += texts[idx]
                        idx += 1
                    value += texts[idx]
            res[field] = value
            idx += 1
        else:
            if start_key.search(texts[idx]):
                template_flag = True
            idx += 1
    return res

if __name__ == '__main__':
    with open('wiki_england.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if line != '']

    print(get_template(lines, "基礎情報"))
