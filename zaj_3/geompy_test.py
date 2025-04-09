import geompy

print("Kwadrat:")
kwadrat = geompy.figury2d.Kwadrat(2)
print(f"Pole: {kwadrat.oblicz_pole()}")
print(f"Obwod: {kwadrat.oblicz_obwod()}")

print("Prostokat:")
prostokat = geompy.figury2d.Prostokat(2, 3)
print(f"Pole: {prostokat.oblicz_pole()}")
print(f"Obwod: {prostokat.oblicz_obwod()}")

print("Kolo:")
kolo = geompy.figury2d.Kolo(4)
print(f"Pole: {kolo.oblicz_pole()}")
print(f"Obwod: {kolo.oblicz_obwod()}")

print("Szescian:")
szescian = geompy.figury3d.Szescian(5)
print(f"Objetosc: {szescian.oblicz_objetosc()}")
print(f"Pole powierzchni calkowitej: {szescian.oblicz_pole_powierzchni()}")

print("Kula:")
kula = geompy.figury3d.Kula(5)
print(f"Objetosc: {kula.oblicz_objetosc()}")
print(f"Pole powierzchni calkowitej: {kula.oblicz_pole_powierzchni()}")

print("Prostopadloscian:")
prostopadlocian = geompy.figury3d.Prostopadloscian(5, 2, 3)
print(f"Objetosc: {prostopadlocian.oblicz_objetosc()}")
print(f"Pole powierzchni calkowitej: {prostopadlocian.oblicz_pole_powierzchni()}")
