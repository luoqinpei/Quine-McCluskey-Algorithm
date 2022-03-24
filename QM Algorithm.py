import numpy as np
import math
import cmath

from sklearn.cluster import k_means

def calc(x):
    sum = 0
    while x!=0:
        sum += x&1
        x = x>>1
    return sum

def convert(x):
    s = []
    while x!=0:
        s += str(x&1)
        x = x>>1
    while(len(s)<4):
        s += "0"
    return s

def cmp(x, y):
    sum = 0
    t = ['0'] * 4
    for i in range(4):
        if x[i]!=y[i]:
            t[i]="~"
            sum += 1
        else:
            t[i]=x[i]
    return sum, t

def reconvert(s):
    ans = ''
    k = 64
    for i in range(len(s)-1,-1,-1):
        k += 1
        if s[i]=="~":
            continue
        if s[i]=='0':
            ans += chr(k)
            ans += "'"
        if s[i]=='1':
            ans += chr(k)
    return ans

if __name__=="__main__":
    with open("./in.txt") as f:
        s = f.readline()
    miniterm = []
    PI = {1 : [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

    for i in range(len(s)):
        if s[i]!=" ":
            miniterm.append(int(s[i]))
            n = calc(int(s[i]))
            PI[n].append(convert(int(s[i])))
    b1 = [0] * 8
    b2 = [0] * 8
    while 1:
        flag = 0
        for i in range(1,9):
            if PI[i]==False:
                continue
            temp = []
            for j in range(len(PI[i])):
                for k in range(len(PI[i+1])):
                    n,re = cmp(PI[i][j],PI[i+1][k])
                    if n==1:
                        if re not in temp:
                            temp.append(re)
                        b1[j] = 1
                        b2[k] = 1
                        flag = 1
            for j in range(len(PI[i])):
                if b1[j]==0 and PI[i][j] not in temp:
                    temp.append(PI[i][j])
            PI[i] = temp
            b1 = b2
            b2 = [0] * 8
        if flag == 0:
            break
    ans = ''
    for i in range(1,9):
        for j in range(len(PI[i])):
            ans += reconvert(PI[i][j])
            ans += ' + '
    ans = ans[:len(ans)-3]
    print("F = %s"%ans)
    pass