from random import randrange

#Eleitores de cada candidato e o total

a = 3000
b = 7000
total = a + b

pchapeu = 0
pchapeu_medio = 0

repetir = 2000

# ----- Usando n = 20 -------

n = 20

while repetir > 0:
  pchapeu = 0
  i = n
  while i > 0:
    x = randrange(total)  #Amostra 1 eleitor
    if x <= a:
      pchapeu += 1        #Só adiciona ao pchapeu se for eleitor do A
    i = i -1
  
  pchapeu = pchapeu/n         #Ajusta o pchapeu pra proporcao
  pchapeu_medio += pchapeu
  repetir = repetir - 1

pchapeu_medio = pchapeu_medio/2000              #Faz a media depois de 2000 amostragens de tamanho n
desvio = pchapeu_medio*(1 - pchapeu_medio)/n

print("Para n = 20,o p chapeu médio é = ", pchapeu_medio, "\n     e seu desvio padrao é:", desvio)


# ----- Usando n = 100 -------

n = 100

pchapeu = 0
pchapeu_medio = 0

repetir = 2000

while repetir > 0:
  pchapeu = 0
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

print("Para n = 100,o p chapeu médio é = ", pchapeu_medio, "\n     e seu desvio padrao é:", desvio)
