# Zadanie 1
# Paula FLamer

# Zagadnienie 1 - zip()
# Krótkie wyjaśnienie:
# Funkcja zip() służy do łączenia wielu iterowalnych obiektów (np. list, krotek) w jedną sekwencję par (krotek).
# Elementy są łączone według kolejności – pierwszy z pierwszym, drugi z drugim itd.
# Link do dokumentacji zip(): https://docs.python.org/3/library/functions.html#zip 

# Zagadnienie 2 - random
# Krótkie wyjaśnienie:
# Moduł random służy do generowania liczb losowych oraz wykonywania operacji losowych na sekwencjach (np. listach).
# Link do dokumentacji random.choice(): https://docs.python.org/3/library/random.html 

# Zagadnienie 3 - ValueError
# Krótkie wyjaśnienie:
# ValueError to typ błędu (wyjątek), który występuje, gdy funkcja otrzymuje argument poprawnego typu, ale o nieodpowiedniej wartości.
# Link do dokumentacji ValueError: https://docs.python.org/3/library/exceptions.html#ValueError

import random  # importujemy moduł standardowy

# Tworzenie dwóch list: imiona i stanowiska
names = ["Paula", "Natalia", "Dorota"]
roles = ["Developer", "Designer", "Tester"]

# Łączenie elementów dwóch list przy użyciu funkcji zip() – tworzenie par (imię, stanowisko)
employees = list(zip(names, roles))
print("Lista pracowników (imię + stanowisko):")
print(employees)

# Wybór losowego pracownika z listy przy użyciu random.choice() – użycie funkcji z modułu random
chosen = random.choice(employees)
print("\nWylosowany pracownik do zadania:")
print(chosen)

# Obsługa wyjątku – np. błędne przekształcenie tekstu na liczbę
try:
    number = int(input("\nPodaj liczbę całkowitą: "))
    print(f"Twój numer to: {number}")
except ValueError:
    print("To nie była liczba całkowita! Spróbuj ponownie.")
