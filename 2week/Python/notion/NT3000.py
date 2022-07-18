with open('00.txt','w', encoding='utf-8') as f:
    name = "N회차 강동현\n"
    f.write(name)
    greeting = "Hello, Python!\n"
    f.write(greeting)
    for i in range(1, 6):
        data = "%d일차 파이썬 공부 중\n" %i
        f.write(data)