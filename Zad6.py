# Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
    return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "Błąd"
    return a / b

# Wyświetl listę operacji
print("Wybierz operację:")
print("a. Dodawanie")
print("b. Odejmowanie")
print("c. Mnożenie")
print("d. Dzielenie")

# Pozwól użytkownikowi wybrać żądane działanie na podstawie wyświetlonej listy poleceń
op = input("Wpisz wybór (a / b / c / d): ")

# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczby całkowitych
num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))

# Logika do wykonywania określonej operacji za pomocą instrukcji IF -ELIF -ELSE.
if op == 'a':
    print("Wynik: ", add(num1, num2))
elif op == 'b':
    print("Wynik: ", subtract(num1, num2))
elif op == 'c':
    print("Wynik: ", multiply(num1, num2))
elif op == 'd':
    print("Wynik: ", divide(num1, num2))
else:
    # Jeśli użytkownik wybierze operację, która nie jest dostępna, wyświetl komunikat o błędzie
    print("Błąd")
