with open("numbers.txt", "r", encoding="utf-8") as source:
    with open("copy.txt", "w", encoding="utf-8") as target:
        for line in source:
            target.write(line)
