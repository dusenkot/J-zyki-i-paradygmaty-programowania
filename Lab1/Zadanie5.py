def harmonogram_proceduralny(zadania):
    zadania.sort(key=lambda x: x[1])

    ostatnie_zakonczenie = 0
    wybrane_zadania = []
    maks_nagroda = 0

    for zadanie in zadania:
        start, koniec, nagroda = zadanie
        if start >= ostatnie_zakonczenie:
            wybrane_zadania.append(zadanie)
            ostatnie_zakonczenie = koniec
            maks_nagroda += nagroda

    return maks_nagroda, wybrane_zadania

from functools import reduce

def harmonogram_funkcyjny(zadania):
 
    posortowane_zadania = sorted(zadania, key=lambda x: x[1])

    def wybierz_zadania(acc, zadanie):
        ostatnie_zadanie = acc[-1] if acc else None
        if not ostatnie_zadanie or zadanie[0] >= ostatnie_zadanie[1]:
            acc.append(zadanie)
        return acc

    wybrane_zadania = reduce(wybierz_zadania, posortowane_zadania, [])
    maks_nagroda = sum(zadanie[2] for zadanie in wybrane_zadania)

    return maks_nagroda, wybrane_zadania

zadania = [
    (1, 3, 50),
    (2, 5, 20),
    (3, 9, 100),
    (6, 8, 70),
    (9, 11, 60),
    (8, 10, 80)
]


maks_nagroda_p, wybrane_zadania_p = harmonogram_proceduralny(zadania)
print("\n[Proceduralne podejście]")
print("Maksymalna nagroda:", maks_nagroda_p)
print("Wybrane zadania:", wybrane_zadania_p)


maks_nagroda_f, wybrane_zadania_f = harmonogram_funkcyjny(zadania)
print("\n[Funkcyjne podejście]")
print("Maksymalna nagroda:", maks_nagroda_f)
print("Wybrane zadania:", wybrane_zadania_f)
