def comparar_paises(y, x):
  if y < x:
    return True, False
  else:
    return False, True

y = "Barbados"
x = "Bangladesh"

resultado1, resultado2 = comparar_paises(y, x)

print(f"El resultado de {y} viene primero en el diccionario que {x} es {resultado1}.")
print(f"El resultado de {x} viene primero en el diccionario que {y} es {resultado2}.")
