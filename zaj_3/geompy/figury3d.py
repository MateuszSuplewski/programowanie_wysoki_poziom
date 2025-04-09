import math


class Szescian:
    def __init__(self, dlugosc_krawedzi):
        self.dlugosc_krawedzi = dlugosc_krawedzi

    def oblicz_objetosc(self):
        return self.dlugosc_krawedzi * self.dlugosc_krawedzi * self.dlugosc_krawedzi

    def oblicz_pole_powierzchni(self):
        return 6 * self.dlugosc_krawedzi * self.dlugosc_krawedzi


class Prostopadloscian:
    def __init__(self, dlugosc_krawedzi_a, dlugosc_krawedzi_b, wysokosc):
        self.dlugosc_krawedzi_a = dlugosc_krawedzi_a
        self.dlugosc_krawedzi_b = dlugosc_krawedzi_b
        self.wysokosc = wysokosc

    def oblicz_objetosc(self):
        return self.dlugosc_krawedzi_a * self.dlugosc_krawedzi_b * self.wysokosc

    def oblicz_pole_powierzchni(self):
        return 2 * (
            self.dlugosc_krawedzi_a * self.dlugosc_krawedzi_b
            + self.dlugosc_krawedzi_a * self.wysokosc
            + self.dlugosc_krawedzi_b * self.wysokosc
        )


class Kula:
    def __init__(self, promien):
        self.promien = promien

    def oblicz_objetosc(self):
        return 4 / 3 * self.promien * self.promien * self.promien * math.pi

    def oblicz_pole_powierzchni(self):
        return 4 * self.promien * self.promien * math.pi
