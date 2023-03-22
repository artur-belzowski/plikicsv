import csv
import sys

# Funkcja do odczytu pliku CSV
def odczytaj_csv(nazwa_pliku):
    dane = []
    with open('in.csv', 'r') as plikcsv:
        czytnik = csv.reader(plikcsv)
        for wiersz in czytnik:
            dane.append(wiersz)
    return dane

# Funkcja do zapisu pliku CSV
def zapisz_csv(nazwa_pliku, dane):
    with open('out.csv', 'w', newline='') as plikcsv:
        zapis = csv.writer(plikcsv)
        for wiersz in dane:
            zapis.writerow(wiersz)

# Główna funkcja programu
if __name__ == '__main__':
    # Sprawdzenie poprawności argumentów wywołania programu
    if len(sys.argv) < 3 or (len(sys.argv) - 2) % 3 != 0:
        print("Sposób użycia: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>")
        print("<zmiana_x> - Zmiana w postaci \"x,y,wartosc\" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast \"wartosc\" to zmiana, która ma trafić na podane miejsce.")
        sys.exit(1)

    # Odczytanie nazw plików oraz zmian z argumentów wywołania programu
    plik_wejsciowy = sys.argv[1]
    plik_wyjsciowy = sys.argv[2]
    zmiany = sys.argv[3:]

    # Odczytanie danych z pliku wejściowego
    dane = odczytaj_csv(plik_wejsciowy)

    # Przetworzenie zmian
    for zmiana in zmiany:
        x, y, wartosc = zmiana.split(',')
        dane[int(y)-1][int(x)-1] = wartosc

    # Wyświetlenie danych w terminalu
    for wiersz in dane:
        print(','.join(wiersz))

    # Zapisanie danych do pliku wyjściowego
    zapisz_csv(plik_wyjsciowy, dane)
