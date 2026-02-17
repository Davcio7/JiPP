# Zapytaj użytkownika o nazwisko

name = input("Jak masz na imię?: ")

# Zapytaj użytkownika o wiek

age = input("Ile masz lat?: ")

# Zapytaj użytkownika o miasto

city = input("W jakim mieście mieszkasz?: ")

# Zapytaj użytkownika o jego zainteresowania

interests = input("Jakie są Twoje zainteresowania?: ")

# Utwórz tekst wyjściowy za pomocą formatowania ciągów

string = "Cześć {}, masz {} lat, mieszkasz w {} i lubisz {}"

output = string.format(name,age,city,interests)

# Wydrukuj tekst wyjściowy
print(output)
