n1 = int(input())
n2 = int(input())

print(str(n2) if (n1 == n2) else max(n1, n2))
print(str(n1) if (n1 == n2) else min(n1, n2))

