# Użyj modułu random

import random

# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci

questions = ["Dlaczego poniedziałek wypada w poniedziałek?\n","Dlaczego ziemia jest płaska\n","Gdzie się pieniądze z komunii?\n"]
answer = ""

# Wybierz losowe pytanie z danej listy za pomocą instrukcji warunkowej

while answer != "to wszystko":
    question = random.choice(questions)

# Zadaj wybrane pytanie za pomocą funkcji input()
# Pytania muszą zachować jednolite formatowanie
# Aby to uzyskać, przekonwertuje wszystkie odpowiedzi na małe litery i usuń wszelkie nadmiarowe spacje

answer = input(question).strip().lower()

# Poczekaj do czasu, aż użytkownik wprowadzi hasło „To wszystko”
# Wyświetl wiadomość

print("zakończone")
