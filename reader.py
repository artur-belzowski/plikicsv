import csv
import sys

# Funkcja do odczytu pliku CSV
def odczytaj_csv(nazwa_pliku):
    dane = []
    with open(nazwa_pliku, 'r') as plikcsv:
        czytnik = csv.reader(plikcsv)
        for wiersz in czytnik:
            dane.append(wiersz)
    return dane

# Funkcja do zapisu pliku CSV
def zapisz_csv(nazwa_pliku, dane):
    with open(nazwa_pliku, 'w', newline='') as plikcsv:
        zapis = csv.writer(plikcsv)
        for wiersz in dane:
            zapis.writerow(wiersz)

# Główna funkcja programu
if __name__ == '__main__':
    # Sprawdzenie poprawności argumentów wywołania programu
    if len(sys.argv) < 3 :
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
        z = zmiana.split(',')
        if len(z) != 3:
            print('Blad!!!!!!')
            quit()
        x, y, wartosc = z
        x = int(x) - 1
        y = int(y) - 1
        if x < 0 or y < 0:
            print('Blad, x i y musza byc wieksze od 0.')
            quit()
        print('Zmiana:', x, y, wartosc)
        print(dane[x][y])
        dane[x][y] = wartosc
        print(dane[x][y])

    # Wyświetlenie danych w terminalu
    for wiersz in dane:
        print(','.join(wiersz))

    # Zapisanie danych do pliku wyjściowego
    zapisz_csv(plik_wyjsciowy, dane)
