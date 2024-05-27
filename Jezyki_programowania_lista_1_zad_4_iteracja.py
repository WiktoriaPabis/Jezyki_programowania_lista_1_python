import unittest

# Korzystałam ze wzoru na ciąg Fibonacciego: https://pl.wikipedia.org/wiki/Ciąg_Fibonacciego
def Fibonacci(sequence, n):
    """
    Funkcja oblicza ciąg Fibonacciego o zadanej liczbie elementów i zapisuje go do listy.

    Args:
        sequence: Lista, do której zostanie zapisany ciąg Fibonacciego.
        n:        Zadana liczba elementów, dla której należy utworzyć ciąg Fibonacciego.

    Raises:
        ValueError: W przypadku, gdy ilość elementów jest niedopuszczalna.
    """
    # n= ilość elementów ciągu
    if n <= 0:
        raise ValueError("Nieprawidłowe wartości")
    sequence.append(1)
    # jeśli jest jeden element
    if n == 1:
        return
    sequence.append(1)
    # jeśli są dwa elementy
    if n == 2:
        return

    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])

def main():
    """
    Funkcja główna programu, która pobiera od użytkownika liczbę elementów ciągu Fibonacciego do
    wygenerowania i wyświetla wynik.
    """
    FibSequence = []
    print("Podaj ilość elementów ciągu: ")
    elem = int(input())
    Fibonacci(FibSequence, elem)
    print("Ciąg Fibonacciego:", FibSequence)

if __name__ == "__main__":
    main()

    #Testy

class TestFibonacci(unittest.TestCase):

    def test_above_zero(self):
        sequence = []
        n = 12

        Fibonacci(sequence, n)

        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], sequence,
            "Nieprawidłowy ciąg Fibonacciego")

    def test_below_zero(self):
        sequence = []
        n = -5

        with self.assertRaises(ValueError):
            Fibonacci(sequence, n)

    def test_zero(self):
        sequence = []
        n = 0

        with self.assertRaises(ValueError):
            Fibonacci(sequence, n)

if __name__ == '__main__':
    unittest.main()

