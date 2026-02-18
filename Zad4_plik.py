#Zadanie: Masz plik numbers.txt z jedną liczbą w każdej linii, na przykład:
#10 3 7 -2
#Napisz program, który:
#odczytuje liczby z pliku
#konwertuje je na int
#oblicza ich sumę
#wyświetla wynik
#Wskazówka: Użyj int(line.strip()) i przechowuj bieżącą sumę w zmiennej.
sum = 0

with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            number = int(line.strip())
            sum += number

print("Suma liczb: ", sum)
