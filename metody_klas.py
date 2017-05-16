class Pracownik(object):

    roczna_podwyzka = 5
    ilosc_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None
        Pracownik.ilosc_pracownikow += 1

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (1/procent)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return " {} - {} ma wynagrodzenie: {} ".format(self.imie, self.stanowisko, self.wynagrodzenie)


emp1 = Pracownik("John Torturo", "aktor")
emp1.ustaw_pensje(5000)
print("Ilosc pracownikow", Pracownik.ilosc_pracownikow)
print(Pracownik.ilosc_pracownikow)

emp2 = Pracownik("John Travolta", "gwiazda")
emp2.ustaw_pensje(8000)
print("Ilosc pracownikow", Pracownik.ilosc_pracownikow)
print(Pracownik.ilosc_pracownikow)
print(emp1)
print(emp2)
print(Pracownik.roczna_podwyzka)
print(emp1.roczna_podwyzka)
print(emp2.roczna_podwyzka)

Pracownik.roczna_podwyzka = 8
print(Pracownik.roczna_podwyzka)
print(emp1.roczna_podwyzka)
print(emp2.roczna_podwyzka)

emp2.roczna_podwyzka = 12
print(Pracownik.roczna_podwyzka)
print(emp1.roczna_podwyzka)
print(emp2.roczna_podwyzka)

print(emp1.__dict__)
print(emp2.__dict__)

