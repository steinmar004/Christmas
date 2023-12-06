def narysuj_czubek():
    print("\t  X")
    print("\t  X")

def dlugosc_choinki_gora():
    print("\t XXX")
    print("\t XXX")

def dlugosc_choinki_srodek():
    print("\tXXXXX")

def narysuj_pien():
    print("\t XXX")



print("Okej, ile środkowych pięter ma mieć nasza choinka?")
liczba_pieter = int(input())
print(f"Okej, choinka będzie miała {liczba_pieter} środkowe piętera.")
narysuj_czubek()
dlugosc_choinki_gora()

for P in range(liczba_pieter):
    dlugosc_choinki_srodek()

dlugosc_choinki_srodek()

narysuj_pien()
















