poteze = [("j", "a"), ("a", "b"), ("b", "j"), ("a", "b"), ("j", "a"),
          ("a", "b"), ("b", "j"), ("a", "b"), ("a", "j"), ("b", "a"),
          ("j", "a"), ("a", "j")]

vrc_a = 0
vrc_b = 0

for ena_poteza in poteze:
    if ena_poteza[0] == 'a' and ena_poteza[1] == 'j':
        vrc_a = 0
    elif ena_poteza[0] == 'b' and ena_poteza[1] == 'j':
        vrc_b = 0
    elif ena_poteza[0] == 'j' and ena_poteza[1] == 'a':
        vrc_a = 7
    elif ena_poteza[0] == 'j' and ena_poteza[1] == 'b':
        vrc_b = 4
    elif ena_poteza[0] == 'a' and ena_poteza[1] == 'b':
        if(vrc_a >= 4):
            if(vrc_b == 0):
                vrc_b = 4
                vrc_a = vrc_a % 4
            else:
                vrc_b = 4
                vrc_a -= 4 - (vrc_a % 4)
        else:
            vrc_b = vrc_b + vrc_a
            if(vrc_b > 4):
                vrc_b = 4
                vrc_a = vrc_b % 4
            else:
                vrc_a = 0
    elif ena_poteza[0] == 'b' and ena_poteza[1] == 'a':
        vrc_a = vrc_b
        vrc_b = 0

    print('a:', vrc_a, 'b:', vrc_b)

stanja = [(7, 0), (3, 4), (3, 0), (0, 3), (7, 3), (6, 4),
          (6, 0), (2, 4), (0, 4), (4, 0), (7, 0), (0, 0)]

poteze = [("j", "a"), ("a", "b"), ("b", "j"), ("a", "b"), ("j", "a"),
          ("a", "b"), ("b", "j"), ("a", "b"), ("a", "j"), ("b", "a"),
          ("j", "a"), ("a", "j")]

for ena_poteza in stanja:
    if (ena_poteza[0] == 7 and ena_poteza[1] == 0) or (ena_poteza[0] == 7 and ena_poteza[1] == 3):
        print("j a")
    elif(ena_poteza[0] ==  0 and (ena_poteza[1] == 4 or ena_poteza[1] == 0)):
        print("a j")
    elif(ena_poteza[0] == 3 or ena_poteza[0] == 6) and (ena_poteza[1] == 0):
        print("b j")
    elif ena_poteza[0] == 4 and ena_poteza[1] == 0:
        print("b a")
    else:
        print("a b")




