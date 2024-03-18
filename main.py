import operacoes as op
from os import system

while True:
    qtd_jogador = int(input("Digite a quantidade de jogador: "))
    
    if qtd_jogador < 2:
        print("Erro! Minimo 2 Jogadores!")
    
    else:
        break

op.nome_jogadores(qtd_jogador)

op.dinheiro_inicial()

system("cls")

while True:
    print("-"*35)
    print("MENU")
    print("1 - Ver status!")
    print("2 - Atribuir Profissão!")
    print("3 - Receber salário!")
    print("4 - Pagar Banco!")
    print("5 - Receber do Banco!")
    print("6 - Pagar jogador!")
    print("7 - Receber presentes!")
    print("0 - Encerrar jogo!")
    print("-"*35)
    
    menu_op = int(input("Digite a operação: "))
    
    if menu_op == 1:
        op.ver_status()

    elif menu_op == 2:
        op.profissao()
    
    elif menu_op == 3:
        pass
    
    elif menu_op == 4:
        pass
    
    elif menu_op == 5:
        pass
    
    elif menu_op == 6:
        pass
    
    elif menu_op == 7:
        pass
    
    elif menu_op == 0:
        pass
    
    else:
        pass
    