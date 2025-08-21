import re

regularEx_1 = r"\b\w{5}\b"

## La palabra seleccionada tiene 5 caracteres
palabra_1 = """'Cause I'm on top of the world, 'ey
I'm on top of the world, 'ey
Waiting on this for a while now
Paying my dues to the dirt
I've been waiting to smile, 'ey
Been holding it in for a while, 'ey
Take it with me if I can
Been dreaming of this since a child
I'm on top of the world"""

resultado = re.findall(regularEx_1,palabra_1)
print(resultado)
