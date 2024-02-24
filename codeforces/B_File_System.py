files = dict()

for _ in range(int(input())):
    file_name = input()

    if files.get(file_name, 0) == 0:
        print("OK")
        files[file_name] = 1

    else:
        file_number = files[file_name]
        new_file_name = file_name + str(file_number)
        print(new_file_name)
        files[file_name] += 1