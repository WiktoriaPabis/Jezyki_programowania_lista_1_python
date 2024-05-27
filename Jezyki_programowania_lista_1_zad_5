
import unittest

# Korzystałam z opisu problemu ze strony: https://pl.wikipedia.org/wiki/Problem_Collatza
def Collatz(sequence, c0):
    """
    Funkcja generuje ciąg Collatza obliczany dla danej liczby początkowej oraz zapisuje go w liście.

    Args:
        sequence: Lista, do której zostaje zapisany ciąg Collatza.
        c0:       Początkowa liczba w ciągu Collatza.

    Raises:
        ValueError: W przypadku podania liczby, która nie jest liczbą naturalną.
    """
    # work jest potrzebna do tego, aby sterować pętlą w przypadku gdy wpadnie w 4, 2, 1 to ustawia się
    # na False i przerywa działanie pętli
    work = True
    Cn = c0
    # licznik pętli
    i = 0
    if Cn <= 0:
        raise ValueError("Nie podano liczby naturalnej")
    while work:
        if Cn % 2 == 0:
            #dzielenie całkowitoliczbowe //
            Cn = Cn // 2
            sequence.append(Cn)
        else:
            Cn = 3 * Cn + 1
            sequence.append(Cn)
        # jeśli są już przynajmniej 3 elementy ciągu
        if i >= 2:
            if sequence[i] == 1 and sequence[i-1] == 2 and sequence[i-2] == 4:
                work = False
        i += 1

def main():
    """
    Funkcja pobiera początkową wartość ciągu Collatza od użytkownika [c0].
    Funkcja wywołuje funkcję collatz oraz wyświetla ciąg Collatza.
    Funkcja wykonuje testy dla wartości c0 w zakresie 1-100 000, po to, aby znaleźć maksymalną
    wartość elementu ciągu, maksymalną długość ciągu dla któregoś z tych c0 oraz podaje te
    wartości c0.
    """
    sequence = []
    print("Podaj początkową wartość c0: ")
    c0 = int(input())
    Collatz(sequence, c0)
    print("Cykl Collatza:", sequence)

    print("Testy na wartościach c0 z zakresu 1-100000")
    sequence_1 = []
    maxCnValue = 0
    c0Value = 0
    maxCollatzLength = 0
    c0CollatzLength = 0
    for c0 in range(1, 100001):
        Collatz(sequence_1, c0)
        # jeśli sequence_1.max jest większa od zapisanej, to przypisuje nową wartość
        if maxCnValue < max(sequence_1):
            maxCnValue = max(sequence_1)
            c0Value = c0
        if maxCollatzLength < len(sequence_1):
            maxCollatzLength = len(sequence_1)
            c0CollatzLength = c0
        # zerowanie ciągu Collatza
        sequence_1 = []

    print("Maksymalna wartość elementu ciągu:", maxCnValue, "dla c0:", c0Value,
          "\nMaksymalna długość ciągu:", maxCollatzLength, "dla c0:", c0CollatzLength)

if __name__ == "__main__":
    main()

#Testy

class TestCollatz(unittest.TestCase):

    def test_valid(self):
        sequence = []
        c0 = 10

        Collatz(sequence, c0)

        result = [5, 16, 8, 4, 2, 1]

        self.assertEqual(result, sequence, "Ciąg Collatza obliczony niepoprawnie")

    def test_invalid(self):
        sequence = []
        c0 = -20

        with self.assertRaises(ValueError):
            Collatz(sequence, c0)

if __name__ == '__main__':
    unittest.main()
