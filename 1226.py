x, y = map(int, input().split())
# 스트링 넣으면 런타임 오류

if x > 0 and y > 0:
    print(1)
elif x < 0 and y < 0:
    print(3)
elif y < 0 < x:
    print(4)
else:
    print(2)