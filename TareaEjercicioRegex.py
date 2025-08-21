import re

# Ejercicio para extraer direcciones IPv4

regularEx_1 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# Indicamos que cada grupo tiene entre 1 y 3 dígitos. Además, cada uno está separado por un punto.

texto = """ El servidor principal está en 192.168.10.9, mientras que el de respaldo se encuentra en 1.1.1.1.  
También configuramos un proxy temporal en 10.0.0.254 para pruebas internas.  
El router viejo tenía la dirección 172.16.5.20, pero ya no lo usamos.  
Por error alguien anotó 999.999.999.999, que claramente no es una IP válida, pero aparece en el registro.  
Finalmente, el firewall responde desde 203.45.67.89."""

resultado = re.findall(regularEx_1,texto)
print(resultado)
