from math import *

# Vaje
# Krog
# Napiši program, ki izračuna površino in obseg kroga, katerega polmer poda uporabnik.
# (Konstanto π boste dobili, če napišete pi, pri čemer mora na začetku programa pisati
# from math import *, kot smo opisali zgoraj.)

"""
temp_p = input("Vpiši polmer kroga: ")
polmer = float(temp_p)
obseg = 2 * pi * polmer
ploscina = pi * pow(polmer, 2)
print("Obseg kroga je: ", obseg)
print("Ploščina kroga je: ", ploscina)
"""

# Pitagorov izrek
# Napiši program, ki uporabnika vpraša po dolžinah katet pravokotnega trikotnika in izpiše
# dolžino hipotenuze. Kot piše na vrhu strani, za koren uporabimo funkcijo sqrt, ki jo dobimo,
# če na začetek programa napišemo from math import *.

"""
k1 = input("Dolžina k1: ")
k2 = input("Dolžina k2: ")
kateta1 = int(k1)
kateta2 = int(k2)
hipotenuza = pow(kateta1, 2)*pow(kateta2, 2)
hipotenuza = sqrt(hipotenuza)
print("Dolžina hipotenuze je: ", hipotenuza)
"""

# Vodnjak
# Če vržemo v vodnjak kamen in je v vodnjaku voda, se čez nekaj časa zasliši čof.
# Napiši program, ki mu uporabnik vpiše, koliko časa je minilo od trenutka, ko smo spustili kamen,
# do trenutka, ko je reklo čof, program pa izpiše globino vodnjaka. Če ne poznaš enačb, si pomagaj z
# wikipedijo

"""
cas = input("Čas? [s]: ")
t = int(cas)
globina = 1/2 * 9.807 * pow(t, 2)
print("Globina vodnjaka je: ", globina, "metrov")
"""

# Indeks telesne teže
# Napiši program, ki uporabnika vpraša, kako velik (v centimetrih) in kako masiven (v kilogramih) je.
# V odgovor naj izpiše indeks telesne mase (BMI) uporabnika.

"""
visina = input("Višina [cm]? ")
masa = input("Masa? [kg]? ")
v = float(visina)/100
m = float(masa)
itm = m/pow(v, 2)
print("ITM je: ", itm)
"""

# Povprečna ocena
# Napiši program, ki mu uporabnik vpiše oceno, ki so jo pri matematiki dobili Ana, Benjamin in Cilka.
# Program naj izračuna in izpiše povprečno oceno.

# Izziv za razmišljujoče tipe: recimo, da ne bi radi izpisali povprečne temveč srednjo oceno.
# Če so Ana, Benjamin in Cilka dobili 3, 2 in 5, bi radi izpisali 3.
# Izziv: sprogramiraj to reč brez uporabe pogojnih stavkov ali česa podobno "naprednega".
# Konkretno, uporabljaj le funkcije input, print, min in max.
# Namig: min in max lahko prejmeta poljubno število argumentov.
# Pomisli tudi na to, da imaš samo tri osebe; pri štirih ta trik ne bi vžgal.

# Še boljši izziv: recimo, da imamo štiri števila, a, b, c in d.
# Izpisati želimo tretje število po velikosti. Še vedno uporabljamo le max in min.
# Namig: mogoče se splača klicati min in max s samo po dvema argumentoma, a večkrat.
# Morda obstaja tudi kakšna rešitev, kjer kličemo z več argumenti. Morda; ne vem. :)

"""
temp_a = input("Ocena ANA: ")
temp_c = input("Ocena CILKA: ")
temp_b = input("Ocena BENJAMIN: ")
ana = int(temp_a)
cilka = int(temp_c)
benjamin = int(temp_b)
p = (ana + cilka + benjamin) / 3
print("Povprečje je: ", p)
"""

# Površina trikotnika
# Napiši program, ki uporabnika vpraša po dolžinah stranic poljubnega trikotnika in izpiše njegovo ploščino,
# ter ploščini včrtanega in očrtanega kroga.


