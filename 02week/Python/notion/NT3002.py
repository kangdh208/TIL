from itertools import count


with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    berries = list()
    for i in f: 
        i = i.strip()
        last5 = ''.join(i[-5:])
        if last5 == 'berry':
            berries.append(i.strip())
    berrys = list(set(berries))
    cnt = len(berrys)
with open('02.txt','w', encoding='utf-8') as f2:
    cnt = str(cnt)
    f2.write(f'{cnt}\n')
    for i in berrys:
        f2.write(f'{i}\n')