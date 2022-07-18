with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0
    for i in f:
        cnt += 1
    print(cnt)
with open('01.txt','w', encoding='utf-8') as f2:
    cnt = str(cnt)
    f2.write(cnt)