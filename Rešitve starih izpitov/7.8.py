# Domača naloga z boti: https://ucilnica.fri.uni-lj.si/mod/assign/view.php?id=17726
# Domača naloga s kraji: https://ucilnica.fri.uni-lj.si/mod/assign/view.php?id=16233


def preveri_vrsto(vrsta, prepovedani):
    p = dict(prepovedani)
    i = 1
    prva = vrsta[0]
    while i < len(vrsta):
        if vrsta[i] in prepovedani[prva]:
            return False
        prva = vrsta[i]
        i += 1
    else:
        return True


def odprepovej(vrsta, prepovedani):
    for oseba1,oseba2 in zip(vrsta,vrsta[1:]):
        for prepovedan in prepovedani:
            if prepovedan[0] == oseba1 and prepovedan[1] == oseba2:
                prepovedani.remove(prepovedan)
            elif prepovedan[1] == oseba1 and prepovedan[0] == oseba2:
                prepovedani.remove(prepovedan)


def najbolj_oddaljena(kraj,kraji):
    for meja1, xm, ym in kraji:
        if meja1 == kraj:
            break

    naj1 = naj2 = naj_razdalja = 0
    for kraj1, x1, y1 in kraji:
        if y1 >= ym:
            continue
        for kraj2, x2, y2 in kraji:
            if y2 >= ym:
                continue
            razdalja = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if razdalja > naj_razdalja:
                naj1, naj2 = kraj1, kraj2
                naj_razdalja = razdalja
    return naj1, naj2


class Ladja:

    def __init__(self, nosilnost):
        self.nosilnost = nosilnost
        self.paketi = []
        self.odstranjeni = 0

    def natovori(self, teza):
        self.paketi.append(teza)
        while sum(self.paketi) > self.nosilnost:
            del self.paketi[0]
            self.odstranjeni += 1

# iteracija skozi seznam ki ga sproti spreminjamo ni pravilen z zanko for ampak je boljši while

    def skupna_teza(self):
        return sum(self.paketi)

    def odstranjenih(self):
        return self.odstranjeni

    def __len__(ladja):
        return len(ladja.paketi)

import unittest

class Test01PreveriVrsto(unittest.TestCase):
    def test_preveri_vrsto(self):
        vrsta = ["Ana", "Berta", "Cilka", "Dani", "Ema"]

        self.assertTrue(preveri_vrsto(vrsta, [("Ana", "Cilka")]))
        self.assertTrue(preveri_vrsto(vrsta, [("Ana", "Cilka"), ("Berta", "Dani")]))

        self.assertFalse(preveri_vrsto(vrsta, [("Ana", "Berta")]))
        self.assertFalse(preveri_vrsto(vrsta, [("Berta", "Ana")]))

        self.assertFalse(preveri_vrsto(vrsta, [("Cilka", "Dani")]))
        self.assertFalse(preveri_vrsto(vrsta, [("Dani", "Cilka")]))

        self.assertFalse(preveri_vrsto(vrsta, [("Dani", "Ema")]))
        self.assertFalse(preveri_vrsto(vrsta, [("Ema", "Dani")]))

        self.assertFalse(preveri_vrsto(vrsta, [("Ana", "Berta"), ("Berta", "Dani")]))
        self.assertFalse(preveri_vrsto(vrsta, [("Berta", "Dani"), ("Ana", "Berta")]))

        self.assertFalse(preveri_vrsto(vrsta, [("Ana", "Cilka"), ("Ana", "Berta"), ("Ana", "Dani")]))
        self.assertFalse(preveri_vrsto(vrsta, [("Ana", "Cilka"), ("Ana", "Berta"), ("Berta", "Dani")]))

        self.assertTrue(preveri_vrsto(vrsta, []))
        self.assertTrue(preveri_vrsto([], [("Ana", "Berta")]))
        self.assertTrue(preveri_vrsto(["Ana", "Berta"], [("Berta", "Cilka")]))

        self.assertFalse(preveri_vrsto(["Ana", "Berta"], [("Berta", "Ana")]))

    def test_preveri_dolgo_vrsto(self):
        self.assertTrue(preveri_vrsto(list(range(10000)), [(x, x + 2) for x in range(10000)]))


class Test02Odprepovej(unittest.TestCase):
    def test_odprepovej(self):
        vrsta = ["Ana", "Berta", "Cilka", "Dani", "Ema"]

        prepovedani = [("Ana", "Cilka")]
        self.assertIsNone(odprepovej(vrsta, prepovedani))
        self.assertEqual(prepovedani, [("Ana", "Cilka")])

        prepovedani = [("Ana", "Cilka"), ("Berta", "Dani")]
        self.assertIsNone(odprepovej(vrsta, prepovedani))
        self.assertEqual(prepovedani, [("Ana", "Cilka"), ("Berta", "Dani")])

        prepovedani = [("Ana", "Cilka"), ("Berta", "Cilka"), ("Berta", "Dani"),
                       ("Ana", "Berta"), ("Dani", "Ema"), ("Dani", "Cilka"),
                       ("Ana", "Ema")]
        self.assertIsNone(odprepovej(vrsta, prepovedani))
        self.assertEqual(prepovedani, [("Ana", "Cilka"), ("Berta", "Dani"),
                               ("Ana", "Ema")])


class Test03NajboljOddaljena(unittest.TestCase):
    def test_najbolj_oddaljena(self):
        kraji = [
            ('Brežice', 68.66, 7.04), ('Lenart', 85.20, 78.75), ('Rateče', -65.04, 70.04),
            ('Ljutomer', 111.26, 71.82), ('Rogaška Slatina', 71.00, 42.00), ('Ribnica', 7.10, -10.50),
            ('Dutovlje', -56.80, -6.93), ('Lokve', -57.94, 19.32), ('Vinica', 43.81, -38.43),
            ('Brtonigla', -71.00, -47.25), ('Kanal', -71.00, 26.25), ('Črnomelj', 39.05, -27.93),
            ('Trbovlje', 29.61, 35.07), ('Beltinci', 114.81, 80.54), ('Domžale', -2.34, 31.50),
            ('Hodoš', 120.70, 105.00), ('Škofja Loka', -23.64, 35.07), ('Velike Lašče', 0.00, 0.00),
            ('Velenje', 33.16, 54.29), ('Šoštanj', 29.61, 57.75), ('Laško', 42.60, 33.29),
            ('Postojna', -29.54, -5.25), ('Ilirska Bistrica', -27.19, -27.93), ('Radenci', 100.61, 84.00),
            ('Črna', 15.41, 66.57), ('Radeče', 39.05, 24.57), ('Vitanje', 47.36, 57.75),
            ('Bled', -37.84, 56.07), ('Tolmin', -63.90, 36.75), ('Miren', -72.14, 7.04),
            ('Ptuj', 87.61, 61.32), ('Gornja Radgona', 97.06, 89.25), ('Plave', -73.34, 21.00),
            ('Novo mesto', 37.91, -3.47), ('Bovec', -76.89, 52.50), ('Nova Gorica', -69.79, 12.29),
            ('Krško', 60.35, 14.07), ('Cerknica', -18.89, -3.47), ('Slovenska Bistrica', 66.31, 57.75),
            ('Anhovo', -72.14, 22.78), ('Ormož', 107.71, 61.32), ('Škofije', -59.14, -27.93),
            ('Čepovan', -60.35, 22.78), ('Murska Sobota', 108.91, 87.57), ('Ljubljana', -8.24, 22.78),
            ('Idrija', -43.74, 17.54), ('Radlje ob Dravi', 41.46, 82.32), ('Žalec', 37.91, 43.79),
            ('Mojstrana', -49.70, 64.79), ('Log pod Mangartom', -73.34, 59.54), ('Podkoren', -62.69, 70.04),
            ('Kočevje', 16.61, -21.00), ('Soča', -69.79, 52.50), ('Ajdovščina', -53.25, 5.25),
            ('Bohinjska Bistrica', -48.49, 47.25), ('Tržič', -22.44, 56.07), ('Piran', -75.69, -31.50),
            ('Kranj', -20.09, 43.79), ('Kranjska Gora', -60.35, 68.25), ('Izola', -68.59, -31.50),
            ('Radovljica', -31.95, 54.29), ('Gornji Grad', 13.06, 49.03), ('Šentjur', 54.46, 40.32),
            ('Koper', -63.90, -29.72), ('Celje', 45.01, 42.00), ('Mislinja', 42.60, 66.57),
            ('Metlika', 48.56, -19.21), ('Žaga', -81.65, 49.03), ('Komen', -63.90, -1.68),
            ('Žužemberk', 21.30, 0.00), ('Pesnica', 74.55, 80.54), ('Vrhnika', -23.64, 14.07),
            ('Dravograd', 28.40, 78.75), ('Kamnik', -1.14, 40.32), ('Jesenice', -40.19, 64.79),
            ('Kobarid', -74.55, 43.79), ('Portorož', -73.34, -33.18), ('Muta', 37.91, 82.32),
            ('Sežana', -54.39, -13.96), ('Vipava', -47.29, 1.79), ('Maribor', 72.21, 75.28),
            ('Slovenj Gradec', 31.95, 71.82), ('Litija', 14.20, 22.78), ('Na Logu', -62.69, 57.75),
            ('Stara Fužina', -52.04, 47.25), ('Motovun', -56.80, -52.50), ('Pragersko', 73.41, 57.75),
            ('Most na Soči', -63.90, 33.29), ('Brestanica', 60.35, 15.75), ('Savudrija', -80.44, -34.96),
            ('Sodražica', 0.00, -6.93),
        ]

        self.assertIn(najbolj_oddaljena("Ljubljana", kraji), {("Brežice", "Savudrija"), ("Savudrija", "Brežice")})


class Test04KdoDobi(unittest.TestCase):
    def test_kdo_dobi(self):
        boti = {1: (('bot', 3), ('bot', 4)),
                2: (('bot', 4), ('output', 0)),
                3: (('output', 5), ('bot', 5)),
                4: (('bot', 5), ('bot', 6)),
                5: (('output', 1), ('bot', 7)),
                6: (('bot', 7), ('output', 4)),
                7: (('output', 2), ('output', 3))}
        self.assertSetEqual(kdo_dobi(1, boti), {1, 3, 4, 5, 6, 7})
        self.assertSetEqual(kdo_dobi(2, boti), {2, 4, 5, 6, 7})
        self.assertSetEqual(kdo_dobi(3, boti), {3, 5, 7})
        self.assertSetEqual(kdo_dobi(4, boti), {4, 5, 6, 7})
        self.assertSetEqual(kdo_dobi(5, boti), {5, 7})
        self.assertSetEqual(kdo_dobi(6, boti), {6, 7})
        self.assertSetEqual(kdo_dobi(7, boti), {7})


class Test05Ladja(unittest.TestCase):
    def test_1_konstruktor(self):
        ladja = Ladja(42)

    def test_2_natovori_teza(self):
        ladja = Ladja(42)
        ladja.natovori(30)
        self.assertEqual(ladja.skupna_teza(), 30)
        ladja.natovori(4)
        self.assertEqual(ladja.skupna_teza(), 34)
        ladja.natovori(7)
        self.assertEqual(ladja.skupna_teza(), 41)

    def test_3_len(self):
        ladja = Ladja(42)
        self.assertEqual(len(ladja), 0)
        ladja.natovori(30)
        self.assertEqual(len(ladja), 1)
        ladja.natovori(4)
        self.assertEqual(len(ladja), 2)
        ladja.natovori(7)
        self.assertEqual(len(ladja), 3)

    def test_4_odstranjevanje(self):
        ladja = Ladja(42)
        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(30)
        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(10)

        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(21)
        self.assertEqual(ladja.odstranjenih(), 1)
        self.assertEqual(ladja.skupna_teza(), 31)
        self.assertEqual(len(ladja), 2)

        ladja.natovori(41)
        self.assertEqual(ladja.odstranjenih(), 3)
        self.assertEqual(ladja.skupna_teza(), 41)
        self.assertEqual(len(ladja), 1)

        ladja.natovori(50)
        self.assertEqual(ladja.odstranjenih(), 5)
        self.assertEqual(ladja.skupna_teza(), 0)
        self.assertEqual(len(ladja), 0)


if __name__ == "__main__":
    unittest.main()
