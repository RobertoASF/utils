"""
creada el 25 oct 2022
autor Roberto Sánchez F.

"""


from itertools import cycle
'''
Función que dado un rut devuelve el rut contcatenado con su dígito verificador
input: (int) RUT
output: (str) RUT con DV (ej: 12345678-9)
'''

def completa_dv(rut):
    digitos = map(int, reversed(str(rut)))
    factor = cycle(range(2, 8))
    calc = sum(d * f for d, f in zip(digitos, factor))
    rutdv = str(rut)+'-'+(str((-calc) % 11))
    return rutdv

