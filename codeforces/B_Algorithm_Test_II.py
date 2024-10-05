q = int(input())

array = []
indexes = dict()

for _ in range(q):
    # command = list(map(str, input().split()))
    command = input().split()

    if command[0] == 'insert':
        x = int(command[1])
        y = int(command[2])

        if y in indexes:
            pos = indexes[y]
            array.insert(pos + 1, x)

            for i in range(pos + 1, len(array)):
                if array[i] not in indexes:
                    indexes[array[i]] = i
        else:
            indexes[y] = len(array)
            array.append(x)


print(array)