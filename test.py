import random
import os
#zadanie 1
def zadanie1():
    print("Ćwiczenie 1: Zmienne i typy danych")  
    int = 3 #liczba całkowita
    float = 21.37 #liczba zmiennoprzecinkowa
    string = "studenciak" #łańcuch znaków
    list = [1, 2, 3] #lista
    dic = {
        "name": "studenciak",
        "age": 21
    } #słownik
    tup = (1, 2, 3) #krotka
    set = {1, 2, 3} #zbiór
    print(int, type(int))
    print(float, type(float))
    print(string, type(string))
    print(list, type(list))
    print(dic, type(dic))
    print(tup, type(tup))
    print(set, type(set))
zadanie1()
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie 2
def zadanie2():
    print("Ćwiczenie 2: Operacje na ciągach znaków")
    tekst = "Studenciak"
    print(len(tekst)) #długość łańcucha znaków
    print(tekst.upper()) #wszystkie znaki na wielkie litery
    print(tekst.lower()) #wszystkie znaki na małe litery
    print(tekst.startswith("H")) #sprawdzenie czy łańcuch zaczyna się od "H"
    print(tekst.count("a")) #liczba wystąpień litery "a" w łańcuchu znaków
zadanie2() 
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie 3
def zadanie3():
    print("Ćwiczenie 3: Operacje matematyczne i funkcje wbudowane")
    print("Podaj dwie liczby do obliczeń")
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    print("Dodawanie:", x + y)
    print("Odejmowanie:", x - y)
    print("Mnożenie:", x * y)
    print("Dzielenie:", x / y if y != 0 else "Nie można dzielić przez 0")
    print("Reszta z dzielenia:", x % y if y != 0 else "Nie można dzielić przez 0")
zadanie3()
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie 4
def zadanie4():
    print("Ćwiczenie 4: Operacje na listach")
    lista = [random.randint(1, 10) for _ in range(10)]
    print("Wylosowane liczby:", lista)

    print("Największa liczba:", max(lista))
    print("Najmniejsza liczba:", min(lista))

    print("Lista posortowana rosnąco:", sorted(lista))
    print("Lista posortowana malejąco:", sorted(lista, reverse=True))

    # Usunięcie wszystkich 3
    lista = [x for x in lista if x != 3]
    print("Lista po usunięciu wszystkich x=3 :", lista)
zadanie4()
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie 5
def zadanie5():
    print("Ćwiczenie 5: Instrukcje warunkowe - sprawdzanie liczb")
    liczba = int(input("Podaj liczbę: "))
    if liczba % 2 == 0:
        print("Liczba jest parzysta.")
    else:
        print("Liczba jest nieparzysta.")
    if liczba > 0:
        print("Liczba jest dodatnia.")
    elif liczba < 0:
        print("Liczba jest ujemna.")
    else:
        print("Liczba jest równa zero.")
    if liczba % 5 == 0:
        print("Liczba jest wielokrotnością 5.")
    else:
        print("Liczba nie jest wielokrotnością 5.")
zadanie5()  
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie6
def zadanie6():
    print("Ćwiczenie 6: Pętla for i operacje na elementach listy")
    lista2 = [random.randint(1, 20) for _ in range(10)]
    print("Lista:", lista2)

    suma = 0
    for liczba in lista2:
        if liczba % 2 == 0:
            print(liczba, "jest parzysta")
        else:
            print(liczba, "jest nieparzysta")
        suma += liczba

    print("Suma:", suma)
    print("Średnia:", suma / len(lista2))
zadanie6()  
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie 7
def zadanie7():
    print("Ćwiczenie 7: Słowniki – podstawowe operacje")
    studenciaki = {
        "Jan": 2.0,
        "Anna": 5.0,
        "Kasia": 3.5
    }
    print("Studenciaki:", studenciaki)

    # Dodanie nowego studenta
    delikwent = input("Podaj imię nowego studenta: ")
    ocenka = float(input("Podaj ocenę nowego studenta: "))
    studenciaki[delikwent] = ocenka
    print("Lista z dodanym studentem:", studenciaki)
    # Aktualizacja oceny
    student_do_poprawki = input("Podaj imię studenta do poprawki z fizyki: ")
    ocenka_poprawka = float(input("Podaj nową ocenę studenta: "))
    studenciaki[student_do_poprawki] = ocenka_poprawka

    print("Lista z poprawką " + student_do_poprawki+":", studenciaki)
    
    # Usunięcie studenta z najniższą oceną
    najgorszy = min(studenciaki, key=studenciaki.get)
    del studenciaki[najgorszy]

    print("Po usunięciu studenta z najgorszą oceną:", studenciaki)
zadanie7()
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')

#zadanie 8
def zadanie8():
    print("Ćwiczenie 8: Funkcje wbudowane – praca z funkcją input i formatowanie tekstu")
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    imie = imie.title()
    nazwisko = nazwisko.title()
    print("Sformatowane imię i nazwisko:" + imie+ " " +nazwisko)
zadanie8()
input("Naciśnij Enter, aby kontynuować...")
os.system('cls' if os.name == 'nt' else 'clear')


