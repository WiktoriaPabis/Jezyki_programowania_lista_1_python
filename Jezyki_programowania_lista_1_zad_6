import sys
import unittest

def komplement(DNA_kod):
    """
    Funkcja przyjmuje sekwencję nici kodującej DNA w kierunku od 5' do 3' i zwraca jej komplementarną
    sekwencję nici matrycowej DNA w kierunku od 3' do 5'.
    Kod komplementarnej nici matrycowej jest tworzony poprzez zamianę każdej zasady na jej
    komplementarną zasadę według reguł: A -> T, T -> A, C -> G, G -> C.

    Args:
        DNA_kod: Ciąg znaków reprezentujący sekwencję nici kodującej DNA, który ma zostać przekształcony na odpowiadającą mu 
                 nić matrycową DNA.

    Returns:
        Ciąg znaków DNA_mat reprezentujący komplementarny kod DNA nici matrycowej, w przypadku poprawności 
        wprowadzonych danych wejściowych.

    Raises:
        ValueError: W przypadku, gdy podana zasada nie istnieje.
    """
    DNA_mat = ""
    for zasada in DNA_kod:
        if zasada == 'A':
            DNA_mat += 'T'
        elif zasada == 'T':
            DNA_mat += 'A'
        elif zasada == 'C':
            DNA_mat += 'G'
        elif zasada == 'G':
            DNA_mat += 'C'
        else:
            raise ValueError("Podano nieprawidłowe wartości")
    
    # [start:stop:step] -> domyslnie start to 0, stop to size, -1 to odwrocenie
    DNA_mat = DNA_mat[::-1]
    
    return DNA_mat

def transkrybuj(DNA_matryc):
    """
    Funkcja przyjmuje sekwencję nici matrycowej DNA w kierunku od 3' do 5' i zwraca jej komplementarną
    sekwencję cząsteczki RNA w kierunku od 5' do 3'.
    Kod komplementarnej sekwencji łańcucha RNA jest tworzony poprzez zamianę każdej zasady na jej
    komplementarną zasadę według reguł: A -> U, T -> A, C -> G, G -> C.

    Args:
        DNA_matryc: Ciąg znaków reprezentujący sekwencję nici matrycowej DNA, który ma zostać przekształcony na odpowiadający 
                    mu łańcuch RNA.

    Returns:
        Ciąg znaków RNA reprezentujący komplementarny kod łańcucha RNA, w przypadku poprawności 
        wprowadzonych danych wejściowych.

    Raises:
        ValueError: W przypadku, gdy podana zasada nie istnieje.
    """
    RNA = ""
    DNA_matryc_1 = DNA_matryc[::-1]
    for zasada in DNA_matryc_1:
        if zasada == 'A':
            RNA += 'U'
        elif zasada == 'T':
            RNA += 'A'
        elif zasada == 'C':
            RNA += 'G'
        elif zasada == 'G':
            RNA += 'C'
        else:
            raise ValueError("Podano nieprawidłowe wartości")
    
    return RNA

def transluj(codons1, mRNA):
    """
    Funkcja przyjmuje słownik stringów oraz sekwencję nici RNA i zwraca listę stringów.
    Tłumaczy sekwencję mRNA na sekwencję aminokwasów za pomocą dostarczonego słownika kodonów.
    Założeniem funkcji jest, że pracuje ona na liczbie zasad azotowych podzielnych przez 3.

    Args:
        codons1: Słownik kodonów, w której klucz to kodon mRNA, a wartością jest odpowiadający aminokwas.
        mRNA:    Sekwencja mRNA do tłumaczenia na aminokwasy.

    Returns:
        Lista aminokwasów, które odpowiadają sekwencji mRNA, z tym założeniem, że podana sekwencja zawiera 
        podzielną przez 3 liczbę zasad azotowych.

    Raises:
        ValueError: W przypadku, gdy liczba zasad azotowych nie jest podzielna przez 3 oraz w przypadku, gdy nie występuje 
                    kodon STOP lub rozpoczynający.
    """
    listAmino = []
    tempCodon = ""
    startTransl = False
    stopTransl = False
    tempListOfCodons = []
    count = 0
    if len(mRNA) % 3 != 0:
        raise ValueError("Nieprawidłowa liczba zasad azotowych, proszę podać ilość zasad azotowych podzielną przez liczbę 3.")
    
    for elem in mRNA:
        tempCodon += elem
        if count == 2:
            if startTransl:
                if tempCodon in ["UAA", "UAG", "UGA"]:
                    stopTransl = True
                    tempListOfCodons.append(tempCodon)
            if (tempCodon == "AUG" or startTransl) and not stopTransl:
                tempListOfCodons.append(tempCodon)
                startTransl = True
            tempCodon = ""
            count = -1
        count += 1

    for elem in tempListOfCodons:
        listAmino.append(codons1.get(elem))

    if not startTransl:
        raise ValueError("Brak kodonu rozpoczynającego")
    if not stopTransl:
        raise ValueError("Brak kodonu STOP")

    return listAmino

def codons():
    """
    Funkcja zwraca słownik, w którym kluczem jest kodon RNA, natomiast wartością odpowiadający mu aminokwas.
    Słownik zawiera zestawienie kodonów RNA, a także aminokwasy im odpowiadające, według standardowego kodu genetycznego.

    Returns:
        Słownik kodonów RNA wraz z odpowiadającymi im aminokwasami.
    """
    codonsMap = {
        # Alanina
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        # Cysteina
        "UGU": "Cys", "UGC": "Cys",
        # Kwas asparaginowy
        "GAU": "Asp", "GAC": "Asp",
        # Kwas glutaminowy
        "GAA": "Glu", "GAG": "Glu",
        # Fenyloalanina
        "UUU": "Phe", "UUC": "Phe",
        # Glicyna
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
        # Histydyna
        "CAU": "His", "CAC": "His",
        # Izoleucyna
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
        # Lizyna
        "AAA": "Lys", "AAG": "Lys",
        # Leucyna
        "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        # Metionina lub kodon rozpoczynający transkrypcję
        "AUG": "Met",
        # Asparagina
        "AAU": "Asn", "AAC": "Asn",
        # Prolina
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        # Glutamina
        "CAA": "Gln", "CAG": "Gln",
        # Arginina
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
        # Seryna
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU": "Ser", "AGC": "Ser",
        # Treonina
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        # Walina
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        # Tryptofan
        "UGG": "Trp",
        # Tyrozyna
        "UAU": "Tyr", "UAC": "Tyr",
        # Kodony STOP
        "UAA": "Ter", "UAG": "Ter", "UGA": "Ter"
    }
    return codonsMap

def main():
    """
    Funkcja główna programu obsługuje wprowadzenie
    """
    print("Proszę wprowadzić odpowiednią sekwencję nici kodującej DNA w kierunku od 5' do 3' z " +
          "możliwych kombinacji zasad azotowych A T G C:  ")
    #strip() usuwa białe znaki
    DNA_kod = input().strip()
    matryca = komplement(DNA_kod)
    print("Sekwencja nici matrycowej w kierunku od 3' do 5': ", matryca)
    nic_RNA = transkrybuj(matryca)
    print("Sekwencja RNA w kierunku od 5' do 3': ", nic_RNA)
    d_Codons = codons()
    AminoList = transluj(d_Codons, nic_RNA)
    print("Sekwencja aminokwasów: ", AminoList)

if __name__ == "__main__":
    main()

#Testy
class komplement_test(unittest.TestCase):

    def test_komplement_valid(self):
        DNA_kod = "ATGCGC"
        matryca = komplement(DNA_kod)
        self.assertEqual("GCGCAT", matryca, "Nieprawidłowo utworzona sekwencja nici matrycowej DNA")

    def test_komplement_invalid(self):
        DNA_kod = "ATGCXYZ"
        with self.assertRaises(ValueError):
            komplement(DNA_kod)

class transkrybuj_test(unittest.TestCase):

    def test_transkrybuj_valid(self):
        DNA_mat = "GCGCAT"
        RNA = transkrybuj(DNA_mat)
        self.assertEqual("AUGCGC", RNA, "Nieprawidłowo utworzona sekwencja nici RNA")

    def test_transkrybuj_invalid(self):
        DNA_mat = "ATGCXYZ2"
        with self.assertRaises(ValueError):
            komplement(DNA_mat)

class transluj_test(unittest.TestCase):

    def test_transluj_valid(self):
        dic_codons = codons()
        AminoList = transluj(dic_codons, "AUGUUUUUCUAG")
        self.assertEqual(["Met", "Phe", "Phe", "Ter"], AminoList, "Nieprawidłowo wykonana translacja")

    def test_transluj_without_start_codon(self):
        dic_codons = codons()
        with self.assertRaises(ValueError):
            transluj(dic_codons, "UUUUUCUAG")

    def test_transluj_without_stop_codon(self):
        dic_codons = codons()
        with self.assertRaises(ValueError):
            transluj(dic_codons, "AUGUUUUUC")

    def test_transluj_invalid_number(self):
        dic_codons = codons()
        with self.assertRaises(ValueError):
            transluj(dic_codons, "AUGUUUA")

if __name__ == '__main__':
    unittest.main()
