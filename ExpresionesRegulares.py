import re # Librería necesaria para utilizar Regex

# \w = toma caracteres como letras, números o el guión bajo _
# \s = espacios en blanco
# \b = establece un límite de palabra

regularEx_1 = r"\b\w{5}\b" # Buscar una palabra que contenga la cantidad de caracteres especificada.

palabra_1 = """'Cause I'm on top of the world, 'ey
I'm on top of the world, 'ey
Waiting on this for a while now
Paying my dues to the dirt
I've been waiting to smile, 'ey
Been holding it in for a while, 'ey
Take it with me if I can
Been dreaming of this since a child
I'm on top of the world
ADD: Are we in Data Structure class?"""

resultado = re.findall(regularEx_1,palabra_1) # Comando para buscar las coincidencias del patrón especificadp dentro del texto.
print(resultado)

regularEx_2 = r"\bchild\b" # Comando para extraer una palabra especifica, 'child'

resultado = re.findall(regularEx_2,palabra_1)
print(resultado)

regularEx_3 = r"\?" # Extraer carácteres especiales

resultado = re.findall(regularEx_3,palabra_1)
print(resultado)
