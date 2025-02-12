def ZnajdzEkstrema(dane):
    najwiekszaLiczba = max(filter(lambda x: isinstance(x, (int, float)), dane), default=None)
    najdluzszyNapis = max(filter(lambda x: isinstance(x, str), dane), key=len, default=None)
    najwiekszaKrotka = max(filter(lambda x: isinstance(x, tuple), dane), key=len, default=None)
    return najwiekszaLiczba, najdluzszyNapis, najwiekszaKrotka

dane = [1, "przykładowy tekts", (1, 2, 3), 4.5, "dłuższy tekst", (1, 2)]
wynik = ZnajdzEkstrema(dane)
print(wynik)
