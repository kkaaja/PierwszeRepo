

# def rysujProstokat(dlugosc, szerokosc, element=4):
#     for i in range(dlugosc):
#         for j in range(szerokosc):
#             print(element, end='')
#         print()
# rysujProstokat(2,3)
# rysujProstokat(2, 3, '*')
print("x")

### Rekurancja uruchamia samą siebie
# def gwiazdki(liczbaGwiazdek):
#     if liczbaGwiazdek > 0:
#         print("*")
#         gwiazdki(liczbaGwiazdek-1)
# gwiazdki(5)

# lista=[1, 2, 3, 4, 5]
# def sumowanie(listaliczb):
#     if len(listaliczb)>0:
#         return listaliczb[0]+sumowanie(listaliczb[1:])
#     else:
#         return 0
# wynik=sumowanie(lista)
# print(wynik)


###
#FUNKCJA MNOŻY REKURENCYJNIE WSZYSTKIE ARGUMENTY LISTY
###
# lista=[1, 2, 3, 4, 5]
# def mnozenie(listaliczb):
#     if len(listaliczb)>0:
#         return listaliczb[0]*mnozenie(listaliczb[1:])
#     else:
#         return 1
# wynik=mnozenie(lista)
# print(wynik)


# def ostatni(listaliczb):
#     if len(listaliczb)>1:
#      return ostatni(listaliczb[1:])
#     else:
#         return listaliczb[0]
# lista=[1, 2, 3, 4, 5]
# wynik=ostatni(lista)
# print(wynik)
#Zawsze musi być warunek końca, zawsze tnie się stringa i zawsze ma być
#określonyostatni element
#
# def dlugosc(listaliczb):
#     if len(listaliczb)>0:
#      return dlugosc(listaliczb[1:])+1
#     else:
#         return 0
# lista=[1, 2, 3, 4, 5]
# wynik=dlugosc(lista)
# print(wynik)
#
# def dlugosc(listaliczb):
#     if listaliczb:
#      return dlugosc(listaliczb[1:])+1
#     else:
#         return 0
# lista=[1, 2, 3, 4, 5]
# wynik=dlugosc(lista)
# print(wynik)



# def maksymalna(listaliczb, zapamietana):
#     if len(listaliczb)>0:
#         if listaliczb[0]>zapamietana:
#             zapamietana=listaliczb[0]
#         return maksymalna(listaliczb[1:], zapamietana)
#     else:
#         return zapamietana
# lista=[1, 2, 3, 4, 5]
# wynik=maksymalna(lista, lista[0])
# print(wynik)

def element(listaliczb, x):
    if len(listaliczb)>0:
        if listaliczb[0]==x:
            return element(listaliczb[1:], x)
    else:
        return x
lista=[1, 2, 3, 4, 5]
elem=4
wynik=element(lista, elem)
print(wynik)
