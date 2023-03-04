import math

def lcm(x, y):
    return x // math.gcd(x, y) * y

def solve():
    n = int(input())
    a = [0] * (n + 2)
    b = [0] * (n + 2)
    a[1:n+1] = list(map(int, input().split()))
    a[0] = a[n+1] = 1
    for i in range(1, n+2):
        b[i] = lcm(a[i-1], a[i])
    for i in range(1, n+1):
        if a[i] != math.gcd(b[i], b[i+1]):
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()



