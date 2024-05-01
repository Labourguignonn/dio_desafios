qt_vitorias = int(input())
qt_derrotas = int(input())

def classificador(rank):
        nível = ''
        if rank <= 10:
            nível = "Ferro"
        elif  rank > 10 and rank <= 20:
            nível = "Bronze"
        elif  rank > 20 and rank <= 50:
            nível = "Prata" 
        elif  rank > 50 and rank <= 80:
            nível = "Ouro"
        elif  rank > 80 and rank <= 90:
            nível = "Diamante"
        elif  rank > 90 and rank <=100:
            nível = "Lendário"
        else:
            nível = "Imortal"    
        return nível
def rankoriasRankeadas(vit,der):
     return vit - der

print(f"O Herói tem de saldo de {rankoriasRankeadas(qt_vitorias,qt_derrotas)} está no nível de {classificador(rankoriasRankeadas(qt_vitorias,qt_derrotas))}")