records = []
for i in range(int(input())):
        records.append([input(), float(input())])

secondHighest = sorted(list(set([b for a,b in records])))[1]

print('\n'.join([a for a,b in sorted(records) if b == secondHighest]))
