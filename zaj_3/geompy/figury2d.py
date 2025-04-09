import math


class Kwadrat:
    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku

    def oblicz_obwod(self):
        return 4 * self.dlugosc_boku

    def oblicz_pole(self):
        return self.dlugosc_boku * self.dlugosc_boku


class Prostokat:
    def __init__(self, dlugosc_boku_a, dlugosc_boku_b):
        self.dlugosc_boku_a = dlugosc_boku_a
        self.dlugosc_boku_b = dlugosc_boku_b

    def oblicz_obwod(self):
        return 2 * self.dlugosc_boku_a + 2 * self.dlugosc_boku_b

    def oblicz_pole(self):
        return self.dlugosc_boku_a * self.dlugosc_boku_b


class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def oblicz_obwod(self):
        return 2 * self.promien * math.pi

    def oblicz_pole(self):
        return self.promien * self.promien * math.pi
