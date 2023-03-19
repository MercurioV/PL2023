import sys
import re
import math
euros = 0
cents = 0
validMoedas = ['5c','10c','20c','50c','1e','2e']
levantar = False
def llamar(cantidad):
    global euros
    global cents
    dif = math.ceil(100 * ((euros+cents/100)-cantidad))/100
    if(dif>=0):
        result = math.modf(dif)
        euros = int(result[1])
        cents = int(result[0]*100)
        print(f"maq: ¨The call was made with a price of {cantidad}e¨")
        print(f"maq: ¨saldo = {euros}e{cents}c¨")
    else:
        print("Not enough money to do the call")

def devolverEuros(euros):
    contador = 0
    while(euros>=2):
        euros -= 2
        contador += 1
    if(euros==1):
        return True,contador
    else:
        return False,contador

def devolverCents(cents):
    contador50 = 0
    contador20 = 0
    contador10 = 0

    while cents >= 50:
        cents -=50
        contador50+=1
    while cents >=20:
        cents-=20
        contador20+=1
    while cents >=10:
        cents-=10
        contador10+=1
    if(cents==5):
        return True,contador50,contador20,contador10
    else:
        return False,contador50,contador20,contador10

def proccessDevolution(euros,cents):
    msg = f"maq: ¨troco={euros}e{cents}c; Volte sempre!¨ ou maq:  ¨troco="
    euro,contador2s = devolverEuros(euros)
    if(contador2s>0):
        msg+=f" {contador2s}x2e,"
    if(euro):
        msg+=f" 1x1e,"
    cinco,contador50,contador20,contador10 = devolverCents(cents)
    if(contador50>0):
        msg+=f" {contador50}x50c,"
    if(contador20>0):
        msg+=f" {contador20}x20c,"
    if(contador10>0):
        msg+=f" {contador10}x10c,"
    if(cinco):
        msg+=f" 1x5c,"
    msg = msg[:-1]
    msg+="; Volte sempre!¨"
    print(msg)
    sys.exit()


def process(line):
    global euros
    global cents
    global levantar
    if "LEVANTAR" in line:
        print("maq: ¨Introduza moedas.¨")
        levantar = True
    elif "MOEDA" in line and levantar:
        listaMoedas = re.sub(r'(MOEDA |\.)','',line).rstrip()
        listaMoedas = re.split(r"\W+",listaMoedas)
        errorMessage = ""
        for moeda in listaMoedas:
            if(moeda in validMoedas):
                if('e' in moeda):
                    euros += int(re.sub('e','',moeda))
                elif('c' in moeda):
                    cents += int(re.sub('c','',moeda))
            else:
                errorMessage+=f" {moeda} - moeda inválida,"
        if(errorMessage):
            print(errorMessage[:-1]+f"; saldo = {euros}e{cents}c")
        else:
            print(f"saldo = {euros}e{cents}c")
    elif "POUSAR" in line and levantar:
        proccessDevolution(euros,cents) 
    elif "T=" in line and levantar:
        tlf = re.sub(r'T=','',line).rstrip()
        if(re.search(r'^(601|641)',tlf) and len(tlf)==9):
            print("maq: ¨Esse número não é permitido neste telefone. Queira discar novo número!¨")
        elif(re.search(r'^00',tlf)):
            llamar(1.5)
        elif(re.search(r'^2',tlf) and len(tlf)==9):
            llamar(0.25)
        elif(re.search(r'^800',tlf) and len(tlf)==9):
            print(f"maq: ¨saldo = {euros}e{cents}c¨")
        elif(re.search(r'^808',tlf) and len(tlf)==9):
            llamar(0.1)
    elif "ABORTAR" in line and levantar:
       proccessDevolution(euros,cents)
    else:
        print("First pick up the phone or enter a valid operation")

for line in sys.stdin:
    process(line)

