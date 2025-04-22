# """
#  Faça um programa que peça ao usuário para digitar um número inteiro,
#  informe se este número é par ou ímpar. Caso o usuário não digite um número
#  inteiro, informe que não é um número inteiro.
#  """
# number = input("Digit a number: ")

# if number.isdigit():
#     number = int(number)
#     if number % 2 == 0:
#         print("This number is even")
#     else:
#         print("this number is odd")
# else:
#     print("You didn't insert an interger number")


#  """
#  Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
#  descrito, exiba a saudação apropriada. Ex.
#  Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
#  """
enter = input('Enter a time in interger numbers: ')

try:
    time = int(enter)

    if time >= 0 and time <= 11:
        print('Good Morning')
    elif time >= 12 and time <= 17:
        print('Good Afternoon')
    elif time >= 18 and time <= 23:
        print('Good Night')
    else:
        print('I don\'t know this time')
except:
    print("You didn't insert an interger number")


#  """
#  Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
#  menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
#  "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
#  """
