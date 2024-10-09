import sys

from Crypto.Util.number import isPrime, long_to_bytes
from sympy import *

# Gegeben sind die folgenden Zahlen:
code_01 = 108162413999135181996156511402797275608781285606390571686953045
code_02 = 108162413999135181996159244248604175263999754594178590687887445
code_03 = 108162413999135181996147323778687510045693508341783380325564501
code_04 = 108162413999135181996159244248604175272433623715066600809824341
code_05 = 108162413999135181996144558818097486901631856364439172989059247

# Mit folgendem Kommando kannst du eine Zahl auf Primzahleigenschaft testen:
print(isPrime(code_05))

# Mit folgendem Kommando kannst du eine Dezimalzahl in einen Bytestring umwandeln:
print(long_to_bytes(code_05))

# Nun bist du an de Reihe, finde die Primzahl und extrahiere das korrekte
# Codewort um die Zeimaschine neu zu kalibrieren!