#Zadanie: Napisz program, który:
#sprawdza czy plik o nazwie data.txt istnieje
#jeśli nie istnieje – tworzy go i zapisuje w nim dowolny tekst
#jeśli już istnieje – wyświetla komunikat: "Plik już istnieje"
#Wskazówka: Użyj import os oraz os.path.exists(). Do zapisu użyj open(..., "w").
import os

filename = "data.txt"

if os.path.exists(filename):
    print("Plik już istnieje")
else:
    with open(filename, "w") as f:
        f.write("Jakieś bazgroły\n")
    print("Utworzyłeś nowy plik")
