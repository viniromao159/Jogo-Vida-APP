jogadores = []

prof_salario = {
    
}

def nome_jogadores(qtd_jogador):
 
    for jogador in range(1, qtd_jogador+1):
        id = jogador
        nome = input(f"Digite o nome do {jogador}º jogador: ")
        jogadores.append([id, nome])

def dinheiro_inicial():
    inicio = int(input("Deseja alterar o valor incial? (Padrão -> R$10.000) 1 - Trocar | 2 - Padrão: "))
    
    if inicio == 1:
        dinheiro_inicial = float(input("Valor inicial: "))
    else:
        dinheiro_inicial = 10000.0
    
    for jogador in range(len(jogadores)):
        jogadores[jogador].append(dinheiro_inicial)

def ver_saldo():
    print("Saldo dos jogadores: ")
    
    for jogador in range(len(jogadores)):
        print(f"Saldo de {jogadores[jogador][1]} -> R${jogadores[jogador][2]}")
        
nome_jogadores(1)
dinheiro_inicial()
ver_saldo()