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
        self.wynagrodzenie += self.wynagrodzenie * (self.roczna_podwyzka /100)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return " {} - {} ma wynagrodzenie: {} ".format(self.imie, self.stanowisko, self.wynagrodzenie)

    @classmethod
    def ustaw_roczna_podwyzke(cls, ilosc_p_proc):
        cls.roczna_podwyzka = ilosc_p_proc


emp1 = Pracownik("John Torturo", "aktor")
emp1.ustaw_pensje(5000)


emp2 = Pracownik("John Travolta", "gwiazda")
emp2.ustaw_pensje(8000)

Pracownik.ustaw_roczna_podwyzke(10)
emp2.roczna_podwyzka = 9


print(Pracownik.roczna_podwyzka)
print(emp1.roczna_podwyzka)
print(emp2.roczna_podwyzka)

print(emp1.wynagrodzenie)
print(emp2.wynagrodzenie)



