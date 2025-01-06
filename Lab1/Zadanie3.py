def optymalizacja_proceduralna(zadania):
    zadania.sort(key=lambda x: x[1])  # x[1] to czas wykonania
    czas_oczkiwania = 0
    calkowity_czas = 0
    optymalna_kolejnosc = []
    for zadanie in zadania:
        czas_oczkiwania += zadanie[1]
        calkowity_czas += czas_oczkiwania
        optymalna_kolejnosc.append(zadanie)
    return optymalna_kolejnosc, calkowity_czas
def optymalizacja_funkcyjna(zadania):
    posortowane_zadania = sorted(zadania, key=lambda x: x[1])
    czas_oczkiwania = 0
    calkowity_czas = reduce(lambda acc, zadanie: acc + czas_oczkiwania + zadanie[1], posortowane_zadania, 0)
    return posortowane_zadania, calkowity_czas
zadania = [
    ("Zadanie1", 3, 50),
    ("Zadanie2", 1, 20),
    ("Zadanie3", 2, 30),
    ("Zadanie4", 4, 40)
]
optymalna_kolejnosc_p, calkowity_czas_p = optymalizacja_proceduralna(zadania)
print("\n[Proceduralne podejście]")
print("Optymalna kolejność zadań:", optymalna_kolejnosc_p)
print("Całkowity czas oczekiwania:", calkowity_czas_p)
optymalna_kolejnosc_f, calkowity_czas_f = optymalizacja_funkcyjna(zadania)
print("\n[Funkcyjne podejście]")
print("Optymalna kolejność zadań:", optymalna_kolejnosc_f)
print("Całkowity czas oczekiwania:", calkowity_czas_f)
