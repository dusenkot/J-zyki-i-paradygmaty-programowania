from functools import reduce

def DodajMacierze(macierzA, macierzB):
    return [[macierzA[i][j] + macierzB[i][j] for j in range(len(macierzA[0]))] for i in range(len(macierzA))]
def MnozMacierze(macierzA, macierzB):
    return [[sum(macierzA[i][k] * macierzB[k][j] for k in range(len(macierzB)))
             for j in range(len(macierzB[0]))] for i in range(len(macierzA))]
def PolaczMacierze(macierzA, macierzB, operacja):
    if operacja == 'dodaj':
        return DodajMacierze(macierzA, macierzB)
    elif operacja == 'mnoz':
        return MnozMacierze(macierzA, macierzB)
def WykonajRedukcje(macierze, operacja):
    return reduce(lambda a, b: PolaczMacierze(a, b, operacja), macierze)

macierze = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
wynik = WykonajRedukcje(macierze, 'dodaj')
print(wynik)
