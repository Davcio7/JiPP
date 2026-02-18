words = ["jabłko", "banan", "wiśnia"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    for word in words:
        file.write(word + "\n")
