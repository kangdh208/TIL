# 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다.

# 색	값	곱
# black	    0	    1
# brown	    1	    10
# red	    2	    100
# orange	3 	    1,000
# yellow	4	    10,000
# green	    5	    100,000
# blue	    6	    1,000,000
# violet	7	    10,000,000
# grey	    8	    100,000,000
# white	    9	    1,000,000,000

resist = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange":3,
    "yellow":4,
    "green":5,
    "blue":6,
    "violet":7,
    "grey":8,
    "white":9
}
num1 = resist[input()]
num2 = resist[input()]
num3 = resist[input()]
print((10*num1+num2)*10**num3)