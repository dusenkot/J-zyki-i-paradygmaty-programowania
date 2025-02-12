import re
from collections import Counter

tekst = """Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji analizy tekstu.
Tekst ten powinien zliczać liczbę słów, zdań i akapitów, a także wykluczać stop words i transformować niektóre wyrazy."""
stopWords = set(["i", "a", "the", "to", "w", "z", "na", "o", "że", "jest", "się", "wtedy", "ale"])

def zliczElementy(tekst):
    akapity = tekst.strip().split('\n')
    liczbaAkapitow = len([p for p in akapity if p])
    zdania = re.split(r'[.!?]+', tekst)
    liczbaZdan = len([s for s in zdania if s.strip()])
    slowa = re.findall(r'\b\w+\b', tekst)
    liczbaSlow = len(slowa)
    return liczbaAkapitow, liczbaZdan, liczbaSlow
def przetworzTekst(tekst):
    slowa = re.findall(r'\b\w+\b', tekst)
    przetworzoneSlowa = [
        slowo[::-1] if slowo.lower().startswith('a') else slowo
        for slowo in slowa if slowo.lower() not in stopWords
    ]
    licznikSlow = Counter(przetworzoneSlowa)
    najczestszeSlowa = licznikSlow.most_common(10)
    return najczestszeSlowa
def analizaTekstu(tekst):
    liczbaAkapitow, liczbaZdan, liczbaSlow = zliczElementy(tekst)
    najczestszeSlowa = przetworzTekst(tekst)
    wynik = f"Liczba akapitów: {liczbaAkapitow}, Liczba zdań: {liczbaZdan}, Liczba słów: {liczbaSlow}, Najczęściej występujące słowa: " + \
             ", ".join([f"{slowo}: {ilosc}" for slowo, ilosc in najczestszeSlowa])
    print(wynik)

analizaTekstu(tekst)
