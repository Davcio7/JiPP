with open("story.txt", "r", encoding="utf-8") as file:
    word_count = 0

    for line in file:
        line = line.strip()
        if line:
            words = line.split()
            word_count += len(words)

print(f"Liczba słów w pliku: {word_count}")
