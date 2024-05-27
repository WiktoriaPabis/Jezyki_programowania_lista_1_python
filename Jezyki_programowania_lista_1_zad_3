
import unittest

def generate(index, subset, L, result):
    """
    Funkcja generuje wszystkie podzbiory zbioru znaków [x].

    Generowanie wszystkich możliwych podzbiorów zbioru znaków [x] realizowane jest przez rekurencję.
    Zastosowano dwa rekurencyjne wywołania funkcji generate w celu uzyskania wszystkich możliwych
    kombinacji zbioru. Wywołania różnią się uwzględnianiem i nie uwzględnianiem na każdym poziomie
    rekurencyjnym danego znaku ze zbioru [x].
    Każdy podzbiór jest zapisywany jako zbiór na liście wynikowej po spełnieniu warunku dotarcia
    do ostatniego poziomu rekurencji.

    Args:
        index:  Zmienna odpowiadająca za liczbę poziomów rekurencji oraz pobieranie znaków
                z początkowej listy.
        subset: Zbiór znaków, dla których generowane są podzbiory.
        L:      Początkowa lista znaków, dla której generowane są podzbiory.
        result: Lista wynikowa zawierająca wygenerowane podzbiory znaków.

    Returns:
        Lista zawierająca wszystkie podzbiory zbioru [x].
    """
    # if index == rozmiar listy
    if index == len(L):
        result.append(subset)
        return

    generate(index + 1, subset.union({L[index]}), L, result)
    generate(index + 1, subset, L, result)

def podzbiory(x):
    """
    Funkcja tworzy listę dla zbioru [x], tworzy wynikową listę zbiorów oraz wywołuje funkcję generate
    z indeksem o wartości 0.

    Args:
        x: Zbiór znaków, dla którego generowane są podzbiory.

    Returns:
        Lista zawierająca wszystkie podzbiory zbioru [x].
    """
    L = list(x)
    result = []

    # index odpowiedzialny za poziom rekurencji
    generate(0, set(), L, result)
    return result

def main():
    """
    Funkcja tworzy zbiór znaków, wywołuje funkcję podzbiory oraz wyświetla listę wszystkich
    podzbiorów zbioru znaków [x].
    Zaimplementowano strukturę danych typu set ze względu na brak konieczności sprawdzania powtórzeń
    znaków w zbiorze.
    """
    x = {'a', 'b', 'c', 'd'}
    result = podzbiory(x)
    print(result)

if __name__ == "__main__":
    main()

    #Testy

class TestPodzbiory(unittest.TestCase):

    def test_define(self):
        x = {'a', 'b', 'c', 'd'}
        result = podzbiory(x)
        subsets = [
            set(),
            {'a'},
            {'b'},
            {'c'},
            {'d'},
            {'a', 'b'},
            {'a', 'c'},
            {'a', 'd'},
            {'b', 'c'},
            {'b', 'd'},
            {'c', 'd'},
            {'a', 'b', 'c'},
            {'a', 'b', 'd'},
            {'a', 'c', 'd'},
            {'b', 'c', 'd'},
            {'a', 'b', 'c', 'd'}
        ]

        self.assertEqual(len(subsets), len(result), "Nieprawidłowa ilość podzbiorów")
        for subset in subsets:
            #Czy subset zawiera sie w result
            self.assertIn(subset, result, "Nieprawidłowo utworzony podzbiór")

    def test_empty(self):
        x = set()
        y = []
        y.append(x)
        result = podzbiory(x)

        self.assertEqual(y, result, "Źle obsłużony przypadek pustego zbioru")

if __name__ == '__main__':
    unittest.main()

