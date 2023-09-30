from random import *
seed(8)
st_iger = 100000
plosca = [0,1,2,3,4,5]
st_metov = 0
pozicija = 0
polje_5 = 0
while(polje_5 != 100):
    kocka = randint(1, 6)
    st_metov += 1
    pozicija = (pozicija + kocka) % 6
    if pozicija == 5:
     polje_5 += 1
print("Število metov je: ", st_metov)

for i in range(0, st_iger):
    seed(i)
    st_metov = 0
    polje_5 = 0
    plosca = [0, 1, 2, 3, 4, 5]
    pozicija = 0

    while(polje_5 != 100):
     st_metov += 1
     kocka = randint(1, 6)
     pozicija = (pozicija + kocka) % 6
     if pozicija == 5:
      polje_5 += 1
    if st_metov < st_iger:
     st_iger = st_metov
     min_metov = st_iger

print("Minimalno število metov: ", min_metov)

