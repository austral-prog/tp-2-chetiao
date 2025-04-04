def earth(y, x):
  if x < y:
    return True, False
  else:
    return False, True

y = "Barbados"
x = "Bangladesh"

resultado1, resultado2 = earth(y, x)

print(f"The result of {x} comes first in the dictionary than {y} is {resultado1}.")
print(f"The result of {y} comes first in the dictionary than {x} is {resultado2}.")
