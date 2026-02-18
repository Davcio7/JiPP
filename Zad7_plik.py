with open("raw.txt", "r", encoding="utf-8") as source:
    lines = source.readlines()

with open("clean.txt", "w", encoding="utf-8") as target:
    for line in lines:
        if line.strip():
            target.write(line)
