if __name__ == '__main__':
    N = int(input())
    list = []
    for a in range(N):
        inputs = input().split()
        if inputs[0] == 'print':
            print(list)
        elif inputs[0] == 'insert':
            list.insert(int(inputs[1]), int(inputs[2]))
        elif inputs[0] == "remove":
            list.remove(int(inputs[1]))
        elif inputs[0] == "append":
            list.append(int(inputs[1]))
        elif inputs[0] == "sort":
            list.sort()
        elif inputs[0] == "pop":
            list.pop()
        else:
            list.reverse()
