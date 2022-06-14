import os
import sys
import random
import time
import sqlite3

conn = sqlite3.connect('forca.db')
c = conn.cursor()

pontos = 6
acertos = 0
tam = []
erradas = []
r = True
player = ['Desafiante', 'Competidor']

so = sys.platform 
if 'win' in so:
    limpa = 'cls'
else:
    limpa = 'clear'

os.system(limpa)


def check(letra):  
    global pontos, palavra, tam, acertos, os, time, erradas

    if letra in palavra:
        if letra in tam:  
            print('Letra repitida')
            time.sleep(0.5)
            os.system(limpa)

        else:   
            for j in range(len(palavra)):
                if letra == palavra[j]:
                    acertos += 1  
                    tam.pop(j)  
                    tam.insert(j, letra) 
                    if acertos == len(palavra):  
                        os.system(limpa)
                        print('\n\n\t\tVocê Venceu | Palavra:', palavra)
                        time.sleep(2.5)
                        pontos = 0
                        os.system(limpa)

    else:  
        if letra in erradas: 
            print('Letra repitida')
            time.sleep(0.5)
            os.system(limpa)

        else:
            pontos -= 1
            erradas.append(letra)  
            os.system(limpa)
            if pontos == 0:
                print('\n\n\t\tSuas chances acabaram, a palavra era:', palavra, '\n')
                time.sleep(2.5)
                os.system(limpa)


def main():
    global os, tam, pontos, erradas, player, random, acertos, time, sys
    global check, letra, palavra, r
    rep = True

    while rep == True:

        pontos = 6
        acertos = 0
        tam = []
        erradas = []

        print('\n\t\tMenu \n')
        print('\t 1 - Desafiante vs CPU \n')
        print('\t 2 - Desafiante vs Competidor \n')
        print('\t 3 - SAIR \n')
        op = input('Escolha uma opção: ')

        if op == '1':
            while r == True:
                os.system(limpa)
                print('\t\tCategorias \n')
                print('\t1 - Animais \n')
                print('\t2 - Objetos \n')
                op1 = input('Escolha uma opção: ')
                choice(op1)
            play()
            r = True

        elif op == '2':
            os.system(limpa)
            palavra = ''
            tam = []
            player_esc = player[random.randint(0, 1)]
            palavra = input('%s digite uma palavra:  ' % player_esc)
            palavra = str.lower(palavra)
            os.system(limpa)
            play()

        elif op == '3':
            time.sleep(0.6)
            c.close()
            conn.close() 
            os.system(limpa)
            rep = False

        else:
            print('Opção Inválida....')
            time.sleep(0.6)
            os.system(limpa)


def play():
    global pontos, erradas, tam, palavra, acertos, os, check

    for i in range(len(palavra)):
        tam.append('_')
    while pontos > 0:
        os.system(limpa)  # HUD do Jogo
        print('Vida:', pontos, '| Total de Letras:', len(palavra),
              '| Acertos:', acertos, '| Letras erradas:', erradas)

        print('\n\t\t-->', tam, '\n')  
        letra = input('Digite um letra: ')
        letra = str.lower(letra)
        check(letra)


def choice(op):
    global palavra, r

   
    if op == '1':
        
        c.execute('SELECT count(*) FROM animais')
        qtd_ani = c.fetchone()[0] 
        esc_ani = random.randint(1, qtd_ani) 

        c.execute('SELECT anipal FROM animais WHERE anicod=?', (esc_ani,)) 
        palavra = c.fetchone()[0] 
        
        r = False

    elif op == '2':
        c.execute('SELECT count(*) FROM objetos')
        qtd_obj = c.fetchone()[0] 
        esc_obj = random.randint(1, qtd_obj) 

        c.execute('SELECT objpal FROM objetos WHERE objcod=?', (esc_obj,)) 
        palavra = c.fetchone()[0] 
        r = False

    else:

        print('Opção Invalida...')
        time.sleep(0.6)


if __name__ == '__main__':
    main()

