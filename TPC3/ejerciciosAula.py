import re

def palavra_magica(frase):
  return re.search(r"por favor[.!?]+$", frase) != None



def narcissismo(linha):
  return re.findall(r"[eE][uU]", linha)

def troca_de_curso(linha, novo_curso):
  return re.sub(r"LEI", novo_curso, linha)

def soma_string(linha):
  lista = re.split(',',linha)
  sum = 0
  for number in lista:
    sum+=int(number)
  return sum

def pronomes(linha):
  return re.findall(r"[eE][uU]|[tT][uU]|[eE][lL][eE]|[eE][lL][aA]",linha)

print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))
print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.","prueba"))
print(pronomes("Ele gdg eu tu ggjdjd ela ElE EU"))