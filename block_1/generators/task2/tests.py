def file_log():
    with open("log.txt", "r") as file:
        for f in file:
            if "error" in f.lower():
                yield f


if __name__ == '__main__':
    for i in file_log():
        print(i)
