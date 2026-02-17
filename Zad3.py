# Utwórz zmienne "vowels" (samogłoski) i "consonants" (spółgłoski) i przypisz każdej z nich wartość 0
vowels = 0
consonants = 0

# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”
for i in "Programowanie Pythona":
    print(i)

# Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek w danym łańcuchu znaków
for i in "Programowanie Pythona".lower():
    if i in ['a','ą','e','ę','i','o','u','ó','y']:
        vowels = vowels+1
    elif i in ['b','c','ć','d','f','g','h','j','k','l','ł','m','n','ń','p','r','s','ś','t','w','z','ź','ż']:
        consonants = consonants+1
        
# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków
print("Samogłoski:", vowels)
print("Spółgłoski:", consonants)
