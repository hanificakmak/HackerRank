if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()   #The * is being used to grab additional returns from the split statement.
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    output = list(student_marks[query_name])
    percent = sum(output)/len(output)
    print("%.2f" % percent)
