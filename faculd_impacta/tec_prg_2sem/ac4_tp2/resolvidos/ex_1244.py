# URI Online Judge | 1244
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1244

n = int(input())
for t in range(n):
    c = input().split()
    c.sort(key=len, reverse=True)
    print(' '.join(c))