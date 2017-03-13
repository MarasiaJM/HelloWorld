# -*- coding: cp1250 -*-
print 'Sprawdzam, czy liczba jest całkowita.'
liczba=raw_input("Podaj liczbę:")
if float(liczba)==int(liczba):
    print "Liczba całkowita"
else:
    print "Liczba ułamkowa"
