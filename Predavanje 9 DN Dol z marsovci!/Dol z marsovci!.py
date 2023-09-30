# Funkcije definiraj spodaj, tam, kjer so že zapisane glave, manjka pa vsebina.
# Dokumentacijo funkcij kar pusti, da se navadiš nanjo.

import math
from typing import Tuple, List, Set, Union

# Koordinate so terka floatov in/ali intov
Koordinate = Tuple[Union[float, int], ...]

# Seznam koordinat ladij
Flota = List[Koordinate]

# Seznam skupin ladij (seznam množic koordinat)
Skupine = List[Set[Koordinate]]


############
# Za oceno 6

def razdalja(x: Koordinate, y: Koordinate) -> float:
    """
    Izračunaj razdaljo med točkama s podanima koordinatama.

    Dimenzija točk (`len(x)`) je lahko poljubna, vendar enaka za obe točki.
    Tako kot v dveh dimenzijah tudi (evklidsko) razdaljo v večdimenzionalnem
    prostoru izračunamo kot kvadratni koren vsote kvadratov razlik po
    posamičnih koordinatah.

    Args:
        x: koordinate prve točke
        y: koordinate druge točke

    Returns:
        float: razdalja med točkama
    """

    vsota = 0
    for i in range(len(x)):
        a = x[i]
        b = y[i]
        raz1 = pow(a - b, 2)
        vsota = vsota + raz1

    evklid = math.sqrt(vsota)
    return evklid

def najblizja(marsovec: Koordinate, ladje: Flota) -> Koordinate:
    """
    Poišči našo ladjo, ki je najbližja podani marsovski ladji

    - Klic `najblizja((1, 1), [(0, 0), (5, 2), (-8, 3)]` vrne `(0, 0)`,
      saj je marsovski ladji na koordinatah `(1, 1)` najbližja naša ladja na
      koordinatah `(0, 0)`.

    - Klic `najblizja((-7, 2, 5, 1),
                      [(0, 0, 5, 2), (5, 2, 5, 2), (-8, 3, 5, 2)])`
      vrne `(-8, 3, 5, 2)`.

    Args:
        marsovec: koordinate marsovske ladje
        ladje: koordinate naših ladij

    Returns:
        tuple of float: koordinate najbližje naše ladje
    """

    razdalje = {}

    for cnvl in ladje:
        razdalje.setdefault(cnvl, razdalja(marsovec,cnvl))

    return min(razdalje, key=razdalje.get)


def dodeli_ladje(marsovci: Flota, ladje: Flota) -> Flota:
    """
    Vrni seznam, ki za vsako od podanih marsovskih ladij vsebuje najbližjo našo

    Funkcija vrne seznam terk, ki je enako dolg kot seznam `marsovci`:
    i-ti element rezultata vsebuje koordinate naše ladje, ki je najbližji
    i-ti marsovski ladji.

    - Klic `dodeli_ladje([(1, 1), (0, 0), (-7, 2), (5, 1)],
                         [(0, 0), (5, 2), (-8, 3)])`
      vrne `[(0, 0), (0, 0), (-8, 3), (5, 2)]`, saj je prvima dvema
      marsovcema najbližja ladja na koordinatah `(0, 0)`, tretjemu ladja na
      `(-8, 3)`, četrtemu pa ladja na `(5, 2)`.

    Args:
        marsovci: koordinate marsovskih ladij
        ladje: koordinate naših ladij

    Returns:
        list of tuple of float: seznam enake dolžine kot marsovci, ki vsebuje
            koorindate najbližjih ladij vsaki marsovski ladji
    """
    dodeljene = []

    for marsovci in marsovci:
        dodeljene.append(najblizja(marsovci, ladje))

    return dodeljene



def skupine_marsovcev(marsovci: Flota, ladje: Flota) -> Skupine:
    """
    Razvrsti marsovske ladje v skupine, ki pripadajo posamičnim našim ladjam

    Če bodo za marsovske ladje poskrbele tri naše ladje, se vsaka množica
    nanaša na eno od njih in sicer vsebuje tiste ladje, ki jih bo uničila ta
    naša ladja.

    Vrstni red vrnjenih množic je poljuben.

    Klic

    ```
    skupine_marsovcev(
        [(0, 1), (2, 2), (51, 52), (100, 100),
         (1, 3), (4, 5), (45, 50), (103, 98)],

        [(0, 0), (50, 50), (100, 100)]))
    ```

    vrne

    ```
    [{(0, 1), (2, 2), (1, 3), (4, 5)},
     {(100, 100), (103, 98)},
     {(51, 52), (45, 50)}]
    ```

    Prva množica vsebuje koordinate marsovskih ladij, ki jih uniči ladja na
    koordinatah `(0, 0)`, druga ladje, ki jih uniči ladja na koordinatah
    `(100, 100)` in tretja tiste, ki jih uniči `(50, 50)`.

    Args:
        marsovci: koordinate marsovskih ladij
        ladje: koordinate naših ladij

    Returns:
        list of set of tuple: skupine marsovskih ladij, ki jih uniči ista naša
    """

    vsi = {}
    skupine = []
    cnvl = dodeli_ladje(marsovci, ladje)
    for i in range(len(marsovci)):
        vesoljec = marsovci[i]
        vsi.setdefault(cnvl[i], []).append(vesoljec)

    for k in vsi.keys():
        skupine.append(set(vsi.get(k)))

    return skupine

############
# Za oceno 7

def sredisce(s: Flota) -> Koordinate:
    """
    Poišči središče podane flote

    Funkcija prejme seznam koordinat točk in vrne terko s koordinatami
    njihovega središča. Koordinate te točke so izračunane kot poprečne
    koordinate točk v `s` po vsaki dimenziji posebej.

    Število točk v `s` je poljubno. Točke so poljubno-dimenzionalne.

    Klic sredisce([(2, 8), (6, 10) vrne (4, 9).

    Args:
        s: koordinate točk

    Returns:
        tuple: koordinate sredisca
    """
    vsote = []
    povprecje = []
    i = 0
    k = 0
    x = 0
    st_elementov = 0
    while k < len(s[i]):
        vsota = 0
        while x < len(s):
            vsota = vsota + s[i+x][k]
            x += 1
        vsote.append(vsota)
        k += 1
        st_elementov = x
        x = 0
    for i in vsote:
        povprecje.append(i / st_elementov)

    return tuple(povprecje)


def razpostavi_ladje(skupine: Skupine) -> Flota:
    """
    Poišči optimalno razpostavitev ladij glede na podane skupine.

    Funkcija prejme neko razdelitev marsovskih ladij v skupine in vrne seznam
    koordinat središč teh skupin.

    Klic

    ```
    razpostavi_ladje([{(0, 1), (2, 2), (1, 3), (4, 5)},
                      {(100, 101), (103, 98)},
                      {(51, 52), (45, 50)}])
    ```

    vrne seznam, ki vsebuje

    ```
    [((0 + 2 + 1 + 4) / 4, (1 + 2 + 3 + 5) / 4),
     ((100 + 103) / 2, (101 + 98) / 2),
     ((51 + 45) / 2, (52 + 50) / 2)]
    ```

    Args:
        skupine: seznam skupin, to je, množic koordinat marsovskih ladij

    Returns:
        list of tuple of float: koordinate središč skupin
    """

    seznam = []

    for skupina in skupine:
        seznam.append(sredisce(list(skupina)))

    return seznam


############
# Za oceno 8

def optimiraj_ladje(marsovci: Flota, ladje: Flota) -> Flota:
    """
    Optimiraj pozicije ladij, začenši iz podane pozicije

    Funkcija prejme položaje marsovcev in neko začetno pozicijo naših ladij
    ter izmenično ponavlja naslednja koraka:

    - določi skupine ki pripadajo posamezni naši ladji
    - premakne ladje v središče te skupine

    Ponavljanje se zaključi, ko ni več sprememb.

    Funkcija vrne končne koordinate ladij.

    Args:
        marsovci: koordinate marsovskih ladij
        ladje: koordinate naših ladij

    Returns:
        list of tuple of float: optimirane kordinate naših ladij
    """

    star_polozaj = ladje
    nov_polozaj = []
    while True:
        skupina = skupine_marsovcev(marsovci,star_polozaj)
        nov_polozaj = razpostavi_ladje(skupina)
        if nov_polozaj == star_polozaj:
            break
        else:
            star_polozaj = nov_polozaj
    return nov_polozaj


############
# Za oceno 9


def kvaliteta(marsovci: Flota, ladje: Flota) -> float:
    """
    Vrni vsoto razdalij od vsake marsovske ladje do najbližje naše

    Args:
        marsovci: koordinate marsovskih ladij
        ladje: koordinate naših ladij

    Returns:
        float: vsota razdalij
    """
    vsota = 0

    for marsovec in marsovci:
        cnvl = najblizja(marsovec, ladje)
        r = razdalja(cnvl, marsovec)
        vsota = vsota + r
    return vsota

def nakljucna(marsovci: Flota, ladij: int) -> Flota:
    """
    Sestevi nek naključen razpored podanega števila ladij.

    Koordinate ladij so žrebane iz koordinate marsovskih ladij: za i-to
    koordinato izberemo i-to koordinato neke naključne marsovske ladje.

    Klic

    ```
    nakljucna([(5, 8),
               (2, 17),
               (1, 33),
               (4, 9)], 3)
    ```

    bi lahko vrnil, recimo `[(1, 8), (4, 17), (2, 8)]`. Vsaka prva koordinata
    je žrebana izmed prvih koordinata in druga izmed drugih.

    Args:
        marsovci: položaji marsovskih ladij
        ladij: število naših ladij

    Returns:
        list of tuple of float: naključne koordinate
    """

    vsi = []
    koordinate = []
    k = 0
    st_l = ladij

    for i in range(len(marsovci[k])):
        for j in range(len(marsovci)):
            vsi.append(marsovci[j][i])
        koordinate.append((vsi[:len(marsovci)]))
        vsi.clear()
    rez = []
    polozaj = []
    for z in range(ladij):
        for i in range(len(koordinate)):
            rez.append(random.choice(koordinate[i]))
        polozaj.append(tuple(rez))
        rez.clear()

    return polozaj

# Za oceno 10


def optimiraj_ladje_2(marsovci: Flota, ladje: Flota) -> Tuple[float, Flota]:
    """
    Glej funkcijo :obj:`optimiraj_ladje`.

    Ta funkcija namesto pozicij vrne terko s kvaliteto in pozicijami.

    Args:
        marsovci: koordinate marsovskih ladij
        ladje: koordinate naših ladij

    Returns:
        float: kvaliteta razpostavitve
        list of tuple of float: optimirane kordinate naših ladij
    """

    star_polozaj = ladje
    nov_polozaj = 0
    while True:
        skupina = skupine_marsovcev(marsovci, star_polozaj)
        nov_polozaj = razpostavi_ladje(skupina)
        if nov_polozaj == star_polozaj:
            break
        else:
            star_polozaj = nov_polozaj
    k = kvaliteta(marsovci, nov_polozaj)
    return k, nov_polozaj



def planiraj(marsovci: Flota, ladij: int) -> Flota:
    """
    Poišči optimalen razpored podanega števila naših ladij.

    Funkcija prejme položaj marsovskih ladij in število naših ladij.
    Nato stokrat požene postopek optimizacije, ki ga začne z različnimi
    naključnimi razporedi naših ladij. Vrne najboljši odkriti končni razpored.

    Args:
        marsovci: koordinate marsovskih ladij
        ladij: število naših ladij

    Returns:
        list of tuple of float: najboljše optimirane kordinate naših ladij
    """
    vsi = {}

    i = 0
    while i < 100:
        opt = optimiraj_ladje_2(marsovci, nakljucna(marsovci, ladij))
        vsi.setdefault(opt[0],opt[1])
        i += 1
    naj = min(vsi.keys())
    return vsi.get(naj)

##################################
# ##################################
# Testi

import unittest
from math import sqrt
import random
from functools import reduce
from operator import add
from typing import Sized


marsovci1 = [(0.20545151426835478, 0.19569730586370837),
             (0.15224490098349647, 0.3027892234548336),
             (0.23769794656220833, 0.4038193343898574),
             (0.3408865299025396, 0.6766006339144215),
             (0.35862206766415905, 0.8140015847860539),
             (0.4069917161049393, 0.7048890649762283),
             (0.5101802994452705, 0.8523930269413629),
             (0.5069556562158851, 0.6907448494453249),
             (0.7004342499790063, 0.2926862123613312),
             (0.6020826314827531, 0.18963549920760692),
             (0.6165935260149872, 0.355324881141046),
             (0.6826987122173869, 0.14518225039619648),
             (0.6730247825292308, 0.22600633914421553),
             (0.6182058476296798, 0.26237717908082403),
             (0.8326446223838057, 0.5957765451664025),
             (0.7262313958140891, 0.5553645007923931),
             (0.8003981900899522, 0.5553645007923931),
             (0.3973177864167832, 0.3654278922345483)]


centroidi1 = [(0.248178, 0.316933),
              (0.424727, 0.747726),
              (0.64884, 0.245202),
              (0.786425, 0.568835)]


class TestBase(unittest.TestCase):
    def assertAlmostEqualStruct(self, expected, actual):
        def almost_equal(xs, ys):
            if isinstance(xs, Sized):
                return type(xs) is type(ys) \
                       and len(xs) == len(ys) \
                       and all(almost_equal(x, y) for x, y in zip(xs, ys))
            else:
                return round(abs(xs - ys), 4) == 0

        if not almost_equal(expected, actual):
            self.assertEqual(expected, actual)


class Test06(TestBase):
    def test_01_razdalja(self):
        self.assertAlmostEqual(5, razdalja((5, 12), (2, 16)))
        self.assertAlmostEqual(4, razdalja((1, 7, 4, 2, 6, -7, 4),
                                           (-1, 10, 5, 2, 6, -8, 3)))
        self.assertAlmostEqual(3, razdalja((5, ), (8, )))

    def test_02_najblizja(self):
        self.assertEqual((0, 0), najblizja((1, 1), [(0, 0), (5, 2), (-8, 3)]))
        self.assertEqual((0, 0), najblizja((0, 0), [(0, 0), (5, 2), (-8, 3)]))
        self.assertEqual((-8, 3), najblizja((-7, 2), [(0, 0), (5, 2), (-8, 3)]))

        self.assertEqual((-8, ), najblizja((-7, ), [(0, ), (5, ), (-8, )]))

        self.assertEqual((-8, 3, 5, 2),
                         najblizja((-7, 2, 5, 1),
                                   [(0, 0, 5, 2), (5, 2, 5, 2), (-8, 3, 5, 2)]))

    def test_03_dodeli_ladje(self):
        self.assertEqual([(0, 0), (0, 0), (-8, 3), (5, 2)],
                         dodeli_ladje([(1, 1), (0, 0), (-7, 2), (5, 1)],
                                      [(0, 0), (5, 2), (-8, 3)]))

        self.assertEqual([(0, ), (0, ), (-8, ), (5, )],
                         dodeli_ladje([(1, ), (0, ), (-7, ), (5, )],
                                      [(0, ), (5, ), (-8, )]))

        self.assertEqual([(-8, 3, 5, 2)],
                         dodeli_ladje([(-7, 2, 5, 1)],
                                      [(0, 0, 5, 2), (5, 2, 5, 2), (-8, 3, 5, 2)]))

        self.assertAlmostEqualStruct(
            [(0.248178, 0.316933),
             (0.248178, 0.316933),
             (0.248178, 0.316933),
             (0.424727, 0.747726),
             (0.424727, 0.747726),
             (0.424727, 0.747726),
             (0.424727, 0.747726),
             (0.424727, 0.747726),
             (0.64884, 0.245202),
             (0.64884, 0.245202),
             (0.64884, 0.245202),
             (0.64884, 0.245202),
             (0.64884, 0.245202),
             (0.64884, 0.245202),
             (0.786425, 0.568835),
             (0.786425, 0.568835),
             (0.786425, 0.568835),
             (0.248178, 0.316933)],
            dodeli_ladje(marsovci1, centroidi1))

    def test_04_skupine_marsovcev(self):
        def equal_sets(s, t):
            self.assertAlmostEqualStruct(sorted(sorted(x) for x in s),
                                         sorted(sorted(x) for x in t))

        equal_sets([{(0, 1), (2, 2), (1, 3), (4, 5)},
                    {(100, 100), (103, 98)},
                    {(51, 52), (45, 50)}],
                   skupine_marsovcev(
                       [(0, 1), (2, 2), (51, 52), (100, 100),
                        (1, 3), (4, 5), (45, 50), (103, 98)],
                       [(0, 0), (50, 50), (100, 100)]
                   ))

        equal_sets([{(1, 1), (0, 0)}, {(-7, 2)}, {(5, 1)}],
                   skupine_marsovcev([(1, 1), (0, 0), (-7, 2), (5, 1)],
                                     [(0, 0), (5, 2), (-8, 3)]))

        equal_sets([{(1, ), (0, )}, {(-7, )}, {(5, )}],
                   skupine_marsovcev([(1, ), (0, ), (-7, ), (5, )],
                                     [(0, ), (5, ), (-8, )]))

        equal_sets([{(-7, 2, 5, 1)}],
                   skupine_marsovcev([(-7, 2, 5, 1)],
                                     [(0, 0, 5, 2), (5, 2, 5, 2), (-8, 3, 5, 2)]))

        equal_sets([[(0.15224490098349647, 0.3027892234548336),
                     (0.20545151426835478, 0.19569730586370837),
                     (0.23769794656220833, 0.4038193343898574),
                     (0.3973177864167832, 0.3654278922345483)],
                    [(0.3408865299025396, 0.6766006339144215),
                     (0.35862206766415905, 0.8140015847860539),
                     (0.4069917161049393, 0.7048890649762283),
                     (0.5069556562158851, 0.6907448494453249),
                     (0.5101802994452705, 0.8523930269413629)],
                    [(0.6020826314827531, 0.18963549920760692),
                     (0.6165935260149872, 0.355324881141046),
                     (0.6182058476296798, 0.26237717908082403),
                     (0.6730247825292308, 0.22600633914421553),
                     (0.6826987122173869, 0.14518225039619648),
                     (0.7004342499790063, 0.2926862123613312)],
                    [(0.7262313958140891, 0.5553645007923931),
                     (0.8003981900899522, 0.5553645007923931),
                     (0.8326446223838057, 0.5957765451664025)]],
                   skupine_marsovcev(marsovci1, centroidi1))


class Test07(TestBase):
    def test_01_sredisce(self):
        self.assertEqual(
            (4, 9),
            sredisce([(2, 8), (6, 10)]))
        self.assertEqual(
            (2, 4.5),
            sredisce([(2, 8), (6, 10), (-5, 1), (5, 6), (0, 0), (4, 2)]))
        self.assertEqual(
            (2.0, 6.25, 3.25, 3.75),
            sredisce([(2, 8, 7, 5), (6, 10, 1, 3), (-5, 1, 4, 6), (5, 6, 1, 1)]))
        self.assertEqual(
            (42, ),
            sredisce([(38, ), (40, ), (41, ), (43, ), (44, ), (46, )])
        )

    def test_02_razpostavi_ladje(self):
        self.assertAlmostEqualStruct(
            [((0 + 2 + 1 + 4) / 4, (1 + 2 + 3 + 5) / 4),
             ((100 + 103) / 2, (101 + 98) / 2),
             ((51 + 45) / 2, (52 + 50) / 2)],
            razpostavi_ladje([{(0, 1), (2, 2), (1, 3), (4, 5)},
                              {(100, 101), (103, 98)},
                              {(51, 52), (45, 50)}])
        )

        self.assertAlmostEqualStruct(
            centroidi1,
            razpostavi_ladje([{(0.15224490098349647, 0.3027892234548336),
                               (0.20545151426835478, 0.19569730586370837),
                               (0.23769794656220833, 0.4038193343898574),
                               (0.3973177864167832, 0.3654278922345483)},
                              {(0.3408865299025396, 0.6766006339144215),
                               (0.35862206766415905, 0.8140015847860539),
                               (0.4069917161049393, 0.7048890649762283),
                               (0.5069556562158851, 0.6907448494453249),
                               (0.5101802994452705, 0.8523930269413629)},
                              {(0.6020826314827531, 0.18963549920760692),
                               (0.6165935260149872, 0.355324881141046),
                               (0.6182058476296798, 0.26237717908082403),
                               (0.6730247825292308, 0.22600633914421553),
                               (0.6826987122173869, 0.14518225039619648),
                               (0.7004342499790063, 0.2926862123613312)},
                              {(0.7262313958140891, 0.5553645007923931),
                               (0.8003981900899522, 0.5553645007923931),
                               (0.8326446223838057, 0.5957765451664025)}]))


class Test08(TestBase):
    def test_01_optimiraj_ladje(self):
        marsovci0 = [(0, 1), (2, 2), (51, 52), (100, 101),
                     (1, 3), (4, 5), (45, 50), (103, 98)]
        opti_ladje = {((0 + 2 + 1 + 4) / 4, (1 + 2 + 3 + 5) / 4),
                      ((100 + 103) / 2, (101 + 98) / 2),
                      ((51 + 45) / 2, (52 + 50) / 2)}
        self.assertEqual(
            sorted(opti_ladje),
            sorted(optimiraj_ladje(marsovci0, [(48, 48), (80, 60), (30, 0)])))
        self.assertEqual(
            sorted(opti_ladje),
            sorted(optimiraj_ladje(marsovci0, [(12, 5), (20, 20), (100, 0)])))

        marsovci0 = [(0, 1, 0, 2), (2, 2, 0, 2), (51, 52, 0, 2), (100, 101, 0, 2),
                     (1, 3, 0, 2), (4, 5, 0, 2), (45, 50, 0, 2), (103, 98, 0, 2)]
        opti_ladje = {((0 + 2 + 1 + 4) / 4, (1 + 2 + 3 + 5) / 4, 0, 2),
                      ((100 + 103) / 2, (101 + 98) / 2, 0, 2),
                      ((51 + 45) / 2, (52 + 50) / 2, 0, 2)}
        self.assertEqual(
            sorted(opti_ladje),
            sorted(optimiraj_ladje(marsovci0, [(48, 48, 0, 0), (80, 60, 0, 0), (30, 0, 0, 0)])))

        self.assertAlmostEqualStruct(
            sorted(centroidi1),
            sorted(optimiraj_ladje(marsovci1, [(0.599162, 0.701897),
                                               (0.486312, 0.276537),
                                               (0.415166,	0.610445),
                                               (0.137946, 0.142548)]))
        )
        # Potek:
        [(0.415166, 0.610445), (0.486312, 0.276537), (0.599162, 0.701897), (0.137946, 0.142548)]
        [(0.17884820762592563, 0.249243264659271), (0.3360495650584615, 0.6498276545166404), (0.6752820327898006, 0.6499286846275754), (0.6129082194671182, 0.26237717908082403)]
        [(0.1984647872713532, 0.3007686212361331), (0.36883343789054596, 0.7318304278922346), (0.6752820327898006, 0.6499286846275754), (0.6129082194671182, 0.26237717908082403)]
        [(0.24817803705771072, 0.3169334389857369), (0.42472725386655874, 0.7477258320126783), (0.6488399583088407, 0.24520206022187005), (0.7864247360959489, 0.5688351822503962)]


class Test09(TestBase):
    def test_01_kvaliteta(self):
        marsovci0 = [(0, 1), (2, 2), (51, 52), (100, 101),
                     (1, 3), (4, 5), (45, 50), (103, 98)]

        self.assertAlmostEqual(
            1 + sqrt(2 ** 2 + 2 ** 2) + sqrt(1 + 2 ** 2) + 1 +
            sqrt(1 ** 2 + 3 ** 2) + sqrt(4 ** 2 + 5 ** 2) + 5 + sqrt(3 ** 2 + 2 ** 2),
            kvaliteta(marsovci0, [(0, 0), (50, 50), (100, 100)])
        )

        marsovci0 = [(0, 1, 0, 2), (2, 2, 0, 2), (51, 52, 0, 2), (100, 101, 0, 2),
                     (1, 3, 0, 2), (4, 5, 0, 2), (45, 50, 0, 2), (103, 98, 0, 2)]
        self.assertAlmostEqual(
            1 + sqrt(2 ** 2 + 2 ** 2) + sqrt(1 + 2 ** 2) + 1 +
            sqrt(1 ** 2 + 3 ** 2) + sqrt(4 ** 2 + 5 ** 2) + 5 + sqrt(3 ** 2 + 2 ** 2),
            kvaliteta(marsovci0, [(0, 0, 0, 2), (50, 50, 0, 2), (100, 100, 0, 2)])
        )

        self.assertAlmostEqual(1.5186050917326306,
                               kvaliteta(marsovci1, centroidi1))

    def test_02_nakljucna(self):
        x, y = map(set, zip(*marsovci1))

        for ladij in (3, 5, 100):
            xz, yz = zip(*nakljucna(marsovci1, ladij))
            self.assertEqual(len(xz), ladij)
            self.assertGreater(len(set(xz)), 1)
            self.assertTrue(set(xz) <= x)
            self.assertTrue(set(yz) <= y)

            xz2, yz2 = zip(*nakljucna(marsovci1, ladij))
            self.assertNotEqual(xz, xz2)
            self.assertNotEqual(yz, yz2)

        marsovci = [(0, 1, 2, 3, 4, 5, 6, 7),
                    (8, 9, 10, 11, 12, 13, 14, 15),
                    (16, 17, 18, 19, 20, 21, 22, 23)]
        self.assertTrue(all(x % 8 == i for i, x in enumerate(poz))
                        for poz in nakljucna(marsovci, 10))


class Test10(TestBase):
    def test_01_optimiraj_kvaliteto_2(self):
        marsovci0 = [(0, 1), (2, 2), (51, 52), (100, 101),
                     (1, 3), (4, 5), (45, 50), (103, 98)]
        opti_ladje = {((0 + 2 + 1 + 4) / 4, (1 + 2 + 3 + 5) / 4),
                      ((100 + 103) / 2, (101 + 98) / 2),
                      ((51 + 45) / 2, (52 + 50) / 2)}

        kvaliteta, pozicije = optimiraj_ladje_2(marsovci0, [(48, 48), (80, 60), (30, 0)])

        self.assertEqual(sorted(opti_ladje), sorted(pozicije))
        self.assertAlmostEqual(17.805189087032616, kvaliteta)

    def test_02_planiraj(self):
        for scale in (0.1, 1, 100):
            for _ in range(10):
                centri = [(0, 0, 0), (scale, scale, -scale), (scale, 0, 0)]
                centri = [[x + random.random() * scale / 10 for x in xs] for xs in centri]
                marsovci = [[tuple(random.gauss(x, scale / 10) for x in xs)
                             for _ in range(20)] for xs in centri]
                centroidi = set(map(sredisce, marsovci))
                marsovci = reduce(add, marsovci)
                random.shuffle(marsovci)
                self.assertAlmostEqualStruct(sorted(centroidi), sorted(planiraj(marsovci, 3)))


if __name__ == "__main__":
    unittest.main()
