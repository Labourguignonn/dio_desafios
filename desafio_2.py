qt_vitorias = int(input())
qt_derrotas = int(input())
nível = ""

def classificador(vit):
        nível = ''
        if vit <= 10:
            nível = "Ferro"
        elif  vit > 10 and vit <= 20:
            nível = "Bronze"
        elif  vit > 20 and vit <= 50:
            nível = "Prata" 
        elif  vit > 50 and vit <= 80:
            nível = "Ouro"
        elif  vit > 80 and vit <= 90:
            nível = "Diamante"
        elif  vit > 90 and vit <=100:
            nível = "Lendário"
        else:
            nível = "Imortal"    
        return nível
def vitoriasRankeadas(vit,der):
     return vit - der

print(f"O Herói tem de saldo de {vitoriasRankeadas(qt_vitorias,qt_derrotas)} está no nível de {classificador(qt_vitorias)}")