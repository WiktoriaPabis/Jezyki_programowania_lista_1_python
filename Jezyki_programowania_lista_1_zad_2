
import unittest

def wspolne(x, y):
    """
    Znajduje część wspólną dwóch zbiorów x i y.
    Elementy, które występują w obu listach tymczasowych, są oznaczane jako None w listach 
    tymczasowych [x_temp], [y_temp].

    Args:
        x: Pierwsza lista liczb całkowitych.
        y: Druga lista liczb całkowitych.

    Returns:
        Lista liczb całkowitych, która zawiera elementy wspólne obu list.

    Raises:
        ValueError: W przypadku kiedy nie ma części wspólnej zbioru.
    """
    common_part = []
    x_temp = x[:]
    y_temp = y[:]
    for i in range(len(x_temp)):
        for j in range(len(y_temp)):
            if x_temp[i] == y_temp[j]:
                common_part.append(x_temp[i])
                # zastosowanie zmiennych pomocniczych, aby nie edytować oryginału (None)
                x_temp[i] = None
                y_temp[j] = None
                break
    if len(common_part) == 0:
       raise ValueError("Brak części wspólnej zbiorów x i y")
    return common_part

def main():
    """
    Funkcja main tworzy dwa zbiory [x] i [y] będące listami.
    Występuje wywołanie funkcji wspolne oraz wyświetlenie stosownych komunikatów.
    """
    x = [2, 2, 2, 3, 4, 4, 5]
    y = [2, 2, 8, 9, 4, 4, 4, 5, 5]
    result = wspolne(x, y)
    print("Zbiór x:", x)
    print("Zbiór y:", y)
    print("Część wspólna zbiorów:", result)

if __name__ == "__main__":
    main()

#Testy

class TestWspolne(unittest.TestCase):

    def test_common(self):
        x = [2, 2, 2, 3, 4, 4, 5]
        y = [2, 2, 8, 9, 4, 4, 4, 5, 5]

        result = wspolne(x, y)

        self.assertEqual([2, 2, 4, 4, 5], result, "Elementy wspólne zostały źle obliczone")

    def test_no_common(self):
        x = [9, 12, 18]
        y = [4, 5, 6]

        with self.assertRaises(ValueError):
            wspolne(x, y)

if __name__ == '__main__':
    unittest.main()

