# s = """3
# 1 1
# 2 2
# 3 3"""
s = """3
1 10
0 10
10 10"""

a = s.splitlines()

count = 0

for i in range(1,len(a)):
    p,q = a[i].split()
    if (int(q) - int(p)) >= 2:
        count += 1

print(count)