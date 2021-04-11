# -*- coding:utf-8 -*-

def taoji(n):
    sum = 0
    for i in range(n):
        i = i+1
        if i%2 != 0:
            # print(str(i%2))
            sum = sum + i
            print(str(i),str(sum))
        if i > n:
            break
    return sum

if __name__ == '__main__':
    print(taoji(5))