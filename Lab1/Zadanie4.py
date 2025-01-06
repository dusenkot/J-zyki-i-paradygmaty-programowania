
def plecak_proceduralny(przedmioty, pojemnosc):
    n = len(przedmioty)
    dp = [[0] * (pojemnosc + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, pojemnosc + 1):
            waga, wartosc = przedmioty[i - 1]
            if waga <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - waga] + wartosc)
            else:
                dp[i][w] = dp[i - 1][w]

    w = pojemnosc
    wybrane_przedmioty = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            wybrane_przedmioty.append(przedmioty[i - 1])
            w -= przedmioty[i - 1][0]

    return dp[n][pojemnosc], wybrane_przedmioty

def plecak_funkcyjny(przedmioty, pojemnosc):
    def rekurencyjny_knapsack(pozostale_przedmioty, aktualna_pojemnosc):
        if not pozostale_przedmioty or aktualna_pojemnosc <= 0:
            return 0, []

        pierwszy, *reszta = pozostale_przedmioty
        waga, wartosc = pierwszy

        if waga > aktualna_pojemnosc:
            return rekurencyjny_knapsack(reszta, aktualna_pojemnosc)

        bez_pierwszego = rekurencyjny_knapsack(reszta, aktualna_pojemnosc)
        z_pierwszym = rekurencyjny_knapsack(reszta, aktualna_pojemnosc - waga)
        z_pierwszym = (z_pierwszym[0] + wartosc, [pierwszy] + z_pierwszym[1])

        return max(bez_pierwszego, z_pierwszym, key=lambda x: x[0])

    return rekurencyjny_knapsack(przedmioty, pojemnosc)


przedmioty = [
    (2, 3),  
    (3, 4),  
    (4, 5),  
    (5, 8)   
]

pojemnosc_plecaka = 8

maks_wartosc_p, wybrane_przedmioty_p = plecak_proceduralny(przedmioty, pojemnosc_plecaka)
print("\n[Proceduralne podejście]")
print("Maksymalna wartość:", maks_wartosc_p)
print("Wybrane przedmioty:", wybrane_przedmioty_p)

maks_wartosc_f, wybrane_przedmioty_f = plecak_funkcyjny(przedmioty, pojemnosc_plecaka)
print("\n[Funkcyjne podejście]")
print("Maksymalna wartość:", maks_wartosc_f)
print("Wybrane przedmioty:", wybrane_przedmioty_f)
