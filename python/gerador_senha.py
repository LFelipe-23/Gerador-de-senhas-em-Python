import random
from time import sleep

print('' * 15, 'Esse é um gerador de senhas em Python'.upper())
sleep(1)

fim = False
escolha = int
complexidade = int
senha = ''
verifica = False
s = []
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
letras2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
especial = ['!', '@', '#', '%', '&', '*', '+', '-', '/']


def gerador1(q):
    for i in range(q):
        letra = str(random.choice(letras))
        s.append(letra)


def gerador2(q):
    for i in range(q):
        letra2 = str(random.choice(letras2))
        s.append(letra2)


def gerador3(q):
    for i in range(q):
        chance = random.randint(1, 2)
        if chance == 1:
            letra = str(random.choice(letras))
            s.append(letra)
        elif chance == 2:
            letra2 = str(random.choice(letras2))
            s.append(letra2)


def gerador4(q):
    for i in range(q):
        n = str(random.choice(num))
        s.append(n)


def gerador5(q):
    for i in range(q):

        chance = random.randint(1, 3)
        if chance == 1:
            n = int(random.choice(num))
            s.append(n)
        elif chance == 2:
            letra = str(random.choice(letras))
            s.append(letra)
        elif chance == 3:
            esp = str(random.choice(especial))
            s.append(esp)


while not fim:

    while complexidade:
        print('')
        print('1 - Apenas letras minúsculas')
        print('2 - Apenas letras maiúsculas')
        print('3 - letras maiúsculas e minúsculas')
        print('4 - Apenas números')
        print('5 - Letra, números e caracteres especias')
        print('')

        complexidade = int(input('-'))

        if complexidade == 1 or complexidade == 2 or complexidade == 3 or complexidade == 4 or complexidade == 5:
            break
        else:
            print('Digite uma opição valida (1, 2, 3, 4 ou 5)')

    while escolha:
        print('')
        print('1 - senha simples ( 8 digitos )')
        print('2 - senha media ( 12 digitos )')
        print('3 - senha complexa ( 16 digitos )')
        print('')

        escolha = int(input('-'))

        if escolha == 1 or escolha == 2 or escolha == 3:
            break
        else:
            print('Digite uma opição valida (1, 2 ou 3)')
    if complexidade == 1:
        if escolha == 1:
            gerador1(8)
            for p in range(0, 8):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 2:
            gerador1(12)
            for p in range(0, 12):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 3:
            gerador1(16)
            for p in range(0, 16):
                c = str(s[p])
                senha = str(senha + c)

    elif complexidade == 2:
        if escolha == 1:
            gerador2(8)
            for p in range(0, 8):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 2:
            gerador2(12)
            for p in range(0, 12):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 3:
            gerador2(16)
            for p in range(0, 16):
                c = str(s[p])
                senha = str(senha + c)

    elif complexidade == 3:
        if escolha == 1:
            gerador3(8)
            for p in range(0, 8):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 2:
            gerador3(12)
            for p in range(0, 12):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 3:
            gerador3(16)
            for p in range(0, 16):
                c = str(s[p])
                senha = str(senha + c)

    elif complexidade == 4:
        if escolha == 1:
            gerador4(8)
            for p in range(0, 8):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 2:
            gerador4(12)
            for p in range(0, 12):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 3:
            gerador4(16)
            for p in range(0, 16):
                c = str(s[p])
                senha = str(senha + c)

    elif complexidade == 5:
        if escolha == 1:
            gerador5(8)
            for p in range(0, 8):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 2:
            gerador5(12)
            for p in range(0, 12):
                c = str(s[p])
                senha = str(senha + c)
        elif escolha == 3:
            gerador5(16)
            for p in range(0, 16):
                c = str(s[p])
                senha = str(senha + c)

    print('Sua senha é {}'.format(senha))
    senha = ''
    sleep(2)
    print('')
    print('Encerraar? (1 - Sim  2 - Não)')
    final = str(input(''))
    if final == '1':
        break
    elif final == '2':
        continue
    else:
        print('Opição invalida, gerando nova senha')
        sleep(3)
        continue
