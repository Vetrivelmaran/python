if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        command =input()
        parts = command.split()
        if parts[0] == 'insert':
            list.insert(int(parts[1]), int(parts[2]))
        elif parts[0] == 'print':
            print(list)
        elif parts[0] == 'remove':
            list.remove(int(parts[1]))
        elif parts[0] == 'append':
            list.append(int(parts[1]))
        elif parts[0] == 'sort':
            list.sort()
        elif parts[0] == 'pop':
            list.pop()
        elif parts[0] == 'reverse':
            list.reverse()