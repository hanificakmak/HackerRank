n = int(input())

if n>=2 and n<=10:
    runnerup = list(map(int, input().split()))

print(sorted(list(set(runnerup)))[-2])
