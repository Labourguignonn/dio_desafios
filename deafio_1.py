##Recebendo os inputs de xp e nome do heroi
print("Qual é o nome do seu herói?")
nomeHeroi = input()
print("Qual é a quantidade de esperiência(XP) que seu herói possui?")
quantXP = int(input())

##função que retorna o print de saida
def textNivel(classificação):
    return print(f"O Herói de nome {nomeHeroi} está no nível de {classificação} ")

##condicionais classificadoras de nível
if quantXP <= 1000:
    textNivel("Ferro")
elif quantXP > 1000 and quantXP <= 2000:
    textNivel("Bronze")
elif quantXP > 2000 and quantXP <= 5000:
    textNivel("Prata")
elif quantXP > 5000 and quantXP <= 7000:
    textNivel("Ouro")
elif quantXP > 7000 and quantXP <= 8000:
    textNivel("Platina")
elif quantXP > 8000 and quantXP <= 9000:
    textNivel("Ascendente")
elif quantXP > 9000 and quantXP <= 10000:
    textNivel("Imortal")
elif quantXP >= 10001 :
    textNivel("Radiante")

