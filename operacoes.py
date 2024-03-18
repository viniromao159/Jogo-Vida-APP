jogadores = []

prof_salario = {
    "medico" : 50000.0,
    
}

def nome_jogadores(qtd_jogador):
 
    for jogador in range(1, qtd_jogador+1):
        id = jogador
        nome = input(f"Digite o nome do {jogador}º jogador: ")
        jogadores.append([id, nome])

def ver_jogadores():
    
    for jogador in range(len(jogadores)):
        print(f'{jogador+1} -> {jogadores[jogador][1]}')
        
def dinheiro_inicial():
    
    inicio = int(input("Deseja alterar o valor incial? (Padrão -> R$10.000) 1 - Trocar | 2 - Padrão: "))
    
    if inicio == 1:
        dinheiro_inicial = float(input("Valor inicial: "))
    else:
        dinheiro_inicial = 10000.0
    
    for jogador in range(len(jogadores)):
        jogadores[jogador].append(dinheiro_inicial)

def ver_status():
    
    
    print("\nStatus dos jogadores:\n")
    for jogador in range(len(jogadores)):
        print("-"*35)
        print(f"-Status de {jogadores[jogador][1]}:")
        print(f"-Dinheiro: R${jogadores[jogador][2]}")
        try:
            print(f"-Profissao: R${jogadores[jogador][3]}")
        except:
            print(f"-Não tem profissão!")
        try:
            print(f"-Profissao: R${jogadores[jogador][4]}")
        except:
            print(f"-Não tem seguro!")
        
def profissao():
    
    ver_jogadores()
    
    while True:
        jogador = int(input("\nDigite o número do usuário para atribuir salário: "))
    
        if jogadores[jogador - 1]:
            for profissao, salario in prof_salario.items():
                print(f"{profissao} -> R${salario}")
        else:
            print("Usuário inválido!")
        
        while True:    
            add_profissao = input(f"\nDigite a profissão do jogador {jogador}: ").strip().lower()
        
            if add_profissao in prof_salario.keys():
                jogadores[jogador-1].append(prof_salario[add_profissao])
                break
            else:
                print("Profissão inválido!")
        
        break
        