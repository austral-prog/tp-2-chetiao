def comparar_paises(y, x):
  if y < x:
    return True, False
  else:
    return False, True

y = "Bangladesh"
x = "Barbados"

resultado1, resultado2 = comparar_paises(y, x)

print(f"The result of {y} comes first in the dicctionary than {x} is {resultado1}.")
print(f"The result of {x} comes first in the dicctionary than {y} is {resultado2}.")
