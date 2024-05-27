import math
import unittest

def heron(a, b, c):
    """
    Funkcja oblicza pole trójkąta S wykorzystując wzór Herona.

    Args:
        a: Pierwszy bok trójkąta.
        b: Drugi bok trójkąta.
        c: Trzeci bok trójkąta.

    Returns:
        Pole trójkąta S, jeśli istnieje trójkąt o podanych bokach.

    Raises:
        ValueError: W przypadku, gdy trójkąt o zadanych bokach nie istnieje.
    """
    S = 0
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        # Skorzystałam ze wzoru Herona ze strony: https://pl.wikipedia.org/wiki/Wzór_Herona
        p = 0.5 * (a + b + c)
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S
    else:
        raise ValueError("Trójkąt o zadanych bokach nie istnieje")

def main():
    """
    Funkcja główna programu wywołuje funkcję heron dla ustalonych parametrów długości boków.
    Wyświetla ona obliczone pole trójkąta S.
    """
    a = 3
    b = 4
    c = 5

    heron_1 = heron(a, b, c)
    #Wyświetlanie stringa razem ze zmienną -> print(f"To jest zmienna: {a}") lub print("to...:", a)
    print("Pole trójkąta o zadanych bokach wynosi: {:.2f}".format(heron_1))
     

if __name__ == "__main__":
    main()


#Testy

class test_heron(unittest.TestCase):

    def test_valid(self):
        a = 3.0
        b = 4.0
        c = 5.0

        result = heron(a, b, c)

# AlmostEqual przydatne do zmiennoprzecinkowych, kiedy moe wystąpić problem zaokrągleń
        self.assertAlmostEqual(6.0, result, msg="Błędnie obliczenie pola trójkąta")

    def test_invalid(self):
        a = 2.0
        b = 0.0
        c = 0.0

        with self.assertRaises(ValueError):
            heron(a, b, c)

if __name__ == '__main__':
    unittest.main()
