class Telefon:
    def __init__(self, model, produdent, komunikacja, rozrywka):
        self.model = model
        self.produdent = produdent
        self.komunikacja = komunikacja
        self.rozrywka = rozrywka


class Komunikacja:
    def wyslij_wiadomosc(self,odbiorca, tresc):
        return f"Wyslano wiadomosc do odbiorcy {odbiorca} o tresci {tresc}"

class Rozrywka:
    def odtworz_muzyke(self,utwor):
        return f"Odtwarzanie utworu {utwor}"


komunikacja = Komunikacja()
rozrywka = Rozrywka()
telefon = Telefon("P30 Pro", "Huawei", komunikacja, rozrywka)

print(telefon.komunikacja.wyslij_wiadomosc("Kacper K", "Odbierz brata ze szkoly o 13:00"))
print(telefon.rozrywka.odtworz_muzyke("Twenty One Pilots - The Line"))