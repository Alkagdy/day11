class Pracownik(object):
    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (1/procent)


emp1 = Pracownik("John Turturo", "aktor")
emp2 = Pracownik("John Travolta", "gwiazda")
emp1.ustaw_pensje(5000)
emp2.ustaw_pensje(234567)
print(emp1.wynagrodzenie)
print(emp2.wynagrodzenie)


emp1.daj_podwyzke(10)
emp2.daj_podwyzke(10)
print(emp1.wynagrodzenie)
print(emp2.wynagrodzenie)



