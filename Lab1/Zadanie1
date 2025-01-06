def podzial_paczek(wagi, maks_waga):
    wagi.sort(reverse=True)
    kursy = []

    for waga in wagi:
        dodano_do_kursu = False
        for kurs in kursy:
            if sum(kurs) + waga <= maks_waga:
                kurs.append(waga)
                dodano_do_kursu = True
                break
        
        if not dodano_do_kursu:
            kursy.append([waga])

    return len(kursy), kursy

wagi_paczek = [5, 10, 7, 3, 2, 8]
maksymalna_waga = 15

efektywnosc, lista_kursow = podzial_paczek(wagi_paczek, maksymalna_waga)

print(f"Minimalna liczba kursów: {efektywnosc}")
print("Lista paczek w każdym kursie:")
for i, kurs in enumerate(lista_kursow):
    print(f"Kurs {i + 1}: {kurs}")
