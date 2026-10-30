first = set(map(int, input().split()))
second = set(map(int, input().split()))
print(*sorted(first & second))
