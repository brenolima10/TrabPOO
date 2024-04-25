«import os
from processador import Processador
from pmae import Pmae
from ram import Ram
from armazenamento import Armazenamento
from hd import Hd
from ssd import Ssd
from pdvideo import Pdvideo
from fonte import Fonte
from gabinete import Gabinete


def menu():
    print('------ Assistente de Hardware ------')
    print('>> Digite o número correspondente a opção:')
    print('> (1) - Montar PC')
    print('> (2) - Buscar Hardware')
    print('> (3) - Creditos')
    print('> (4) - Sair')

    return input('> ')

def busca():
    os.system('cls')
    print('------ Assistente de Hardware ------')
    print('                BUSCAR              ')
    print('>> Digite o número correspondente a opção:')
    print('> (1) - Processador')
    print('> (2) - Placa mãe')
    print('> (3) - Memória RAM')
    print('> (4) - HD')
    print('> (5) - SSD')

    b = input('> ')
    if b == '1':
        print('------------------------------------')
        i3_3240.info()
        print('------------------------------------')
        i3_9100F.info()
        print('------------------------------------')
        i3_10100F.info()
        print('------------------------------------')
    elif b == '2':
        print('------------------------------------')
        aFOX_IH61_MA5.info()
        print('------------------------------------')
        asus_H310M_E_R_2_0.info()
        print('------------------------------------')
        asus_Prime_H510M_E.info()
        print('------------------------------------')
    elif b == '3':
        print('------------------------------------')
        kingston_Kvr16n11_4.info()
        print('------------------------------------')
        kingston_HyperX_Fury_HX426C16FB3_4.info()
        print('------------------------------------')
        team_Group_T_force_Vulcan_Tlprd48g3000hc16c01.info()
        print('------------------------------------')
    else:
        print('>> Digito inválido')
    
    input('> ')


#Processador
i3_3240 = Processador(235.00, 'Intel', 'i3-3240', 'FCLGA1155', 3.40, 2, 4, 55)
i3_9100F = Processador(849.99, 'Intel', 'i3-9100F', 'FCLGA1151', 3.60, 4, 4, 65)
i3_10100F = Processador(589.90, 'Intel', 'i3-10100F', 'FCLGA1200', 3.60, 4, 8, 65)

#Placa mãe
aFOX_IH61_MA5 = Pmae(399.55, 'Afox', 'IH61-MA5', 'FCLGA1155', 3, 0)
asus_H310M_E_R_2_0 = Pmae(527.66, 'Asus', 'H310M-E R 2.0', 'FCLGA1151', 4, 0)
asus_Prime_H510M_E = Pmae(625.43, 'Asus', 'H510M-E', 'FCLGA1200', 4, 0)

#Memória RAM
kingston_Kvr16n11_4 = Ram(154.08, 'Kingston', 'Kvr16n11/4', 1600, 3, 1.5)
kingston_HyperX_Fury_HX426C16FB3_4 = Ram(172.40, 'Kingston HyperX', 'HX426C16FB3/4', 2666, 4, 1.2)
team_Group_T_force_Vulcan_Tlprd48g3000hc16c01 = Ram(217.90, 'Team Group', 'Tlprd48g3000hc16c01', 3000, 4, 1.35)

#Falta o resto


os.system('cls')

x = 0

while (x == 0):
    entrada = menu()

    if entrada == '1':
        os.system('cls')
        print('Montar PC')
    elif entrada == '2':
        busca()
        
    elif entrada == '3':
        os.system('cls')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('>> Desenvolvedores:\n>    Deivison\n>    Levi\n>    Bruno\n>    Johnath')
        print('>\n>> (っ◕‿◕)っ\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        input('')
        os.system('cls')
    elif entrada == '4':
        os.system('cls')

        if input('>> Tem certeza que deseja sair?\n>> <ATENÇÃO: As ações feitas não serão salvas>\n>> Digite (1) para confirmar ou (0) para continuar usando o programa.\n> ') == '1':
            print('>> Saindo...')
            x = 1

