def DodajMacierze(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def MnozMacierze(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def TransponujMacierz(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def Walidacja(macierzA, macierzB, operacja):
    if operacja == 'dodaj' and len(macierzA) == len(macierzB) and len(macierzA[0]) == len(macierzB[0]):
        return True
    if operacja == 'mnoz' and len(macierzA[0]) == len(macierzB):
        return True
    return operacja == 'transponuj'
def WykonajOperacje(macierzA, macierzB, operacja):
    if Walidacja(macierzA, macierzB, operacja):
        if operacja == 'dodaj': return DodajMacierze(macierzA, macierzB)
        if operacja == 'mnoz': return MnozMacierze(macierzA, macierzB)
        if operacja == 'transponuj': return TransponujMacierz(macierzA)
    return None

macierz1 = [[1, 2], [3, 4]]
macierz2 = [[5, 6], [7, 8]]

wynik_dodawania = WykonajOperacje(macierz1, macierz2, 'dodaj')
wynik_mnozenia = WykonajOperacje(macierz1, macierz2, 'mnoz')
wynik_transpozycji = WykonajOperacje(macierz1, None, 'transponuj')

print(f"Wynik dodawania: {wynik_dodawania}, "
      f"Wynik mnożenia: {wynik_mnozenia}, "
      f"Wynik transpozycji: {wynik_transpozycji}")
