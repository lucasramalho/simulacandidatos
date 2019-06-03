from random import randrange

a = 3000
b = 7000
total = a + b

pchapeu = 0
pchapeu_medio = 0

repetir = 2000

while repetir > 0:
  pchapeu = 0
  n = 20
  i = n
  while i > 0:
    x = randrange(total)
    if x <= a:
      pchapeu += 1
    i = i -1
  pchapeu = pchapeu/n
  pchapeu_medio += pchapeu
  repetir = repetir - 1

pchapeu_medio = pchapeu_medio/2000
desvio = pchapeu_medio*(1 - pchapeu_medio)/n
print("Para n = 20,o p chapeu médio é = ", pchapeu_medio, "\n     e seu desvio padrao é:", desvio)

pchapeu = 0
pchapeu_medio = 0

repetir = 2000

while repetir > 0:
  pchapeu = 0
  n = 100
  i = n
  while i > 0:
    x = randrange(total)
    if x <= a:
      pchapeu += 1
    i = i -1
  pchapeu = pchapeu/100
  pchapeu_medio += pchapeu
  repetir = repetir - 1

pchapeu_medio = pchapeu_medio/2000
desvio = pchapeu_medio*(1 - pchapeu_medio)/n
print("Para n = 100,o p chapeu médio é = ", pchapeu_medio, "\n     e seu desvio padrao é:", desvio)
