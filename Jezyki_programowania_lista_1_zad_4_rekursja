import unittest

# Korzystałam ze schematu algorytmu na ciąg Fibonacciego: https://www.korepetycjezinformatyki.pl/ciag-fibonacciego/
def Fibonacci_1(sequence, n):
    """
    Funkcja oblicza ciąg Fibonacciego wywołując dla każdego elementu ciągu funkcję fibonacciElement
    i obliczone elementy zapisuje do listy.

    Args:
        sequence: Lista, do której zostanie zapisany ciąg Fibonacciego.
        n:        Zadana liczba elementów, dla której należy utworzyć ciąg Fibonacciego.

    Raises:
        ValueError: W przypadku gdy ilość elementów jest niedopuszczalna.
    """
    if n <= 0:
        raise ValueError("Nie można utworzyć ciągu")
    else:
        for i in range(n):
            sequence.append(fibonacciElement(i))

def fibonacciElement(i):
    """
    Funkcja rekurencyjna oblicza liczbę i-tą w ciągu Fibonacciego.

    Args:
        i: Numer elementu ciągu Fibonacciego.

    Returns:
        Wartość i-tego elementu ciągu Fibonacciego.
    """
    if i <= 1:
        return 1
    else:
        return fibonacciElement(i - 1) + fibonacciElement(i - 2)

def main():
    """
    Funkcja główna programu, która pobiera od użytkownika liczbę elementów ciągu Fibonacciego do
    wygenerowania i wyświetla wynik.
    """
    FibSequence = []
    print("Podaj ilość elementów ciągu: ")
    elem = int(input())
    Fibonacci_1(FibSequence, elem)
    print("Ciąg Fibonacciego:", FibSequence)

if __name__ == "__main__":
    main()

    #Testy

class TestFibonacci(unittest.TestCase):

    def test_above_zero(self):
        sequence = []
        n = 12

        Fibonacci_1(sequence, n)

        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], sequence,
            "Nieprawidłowy ciąg Fibonacciego")

    def test_below_zero(self):
        sequence = []
        n = -5

        with self.assertRaises(ValueError):
            Fibonacci_1(sequence, n)

    def test_zero(self):
        sequence = []
        n = 0

        with self.assertRaises(ValueError):
            Fibonacci_1(sequence, n)

if __name__ == '__main__':
    unittest.main()

