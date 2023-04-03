import random
#zad1
dane = []
for i in range(10):
    dane.append(random.randint(0,30) * 2)
plik = open('liczby.txt', 'w+')
plik.writelines(str(dane))
plik.close()

#zad2
with open('liczby.txt', 'r') as plik1:
     zawartosc = plik1.read()
     print(zawartosc)

#zad3
with open('zdanie.txt', 'w') as plik2:
    plik2.writelines('Testowy tekst \n')
    plik2.writelines('który zostanie zapisany \n')
    plik2.writelines('w tym pliku \n')
    plik2.writelines('o nazwie zdanie.txt \n')
with open('zdanie.txt', 'r') as plik2:
    zawartosc2 = plik2.read()
    print(zawartosc2)

#zad4