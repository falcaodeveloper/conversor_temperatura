import conversor

#Mensagens exibidas ao usuário
msnValor = '\nDigite a temperatura que será convertida:\n'
msnInvalido = 'Digite apenas números!'
msnOpcaoInvalida = '\nEscolha um número de 0 à 4'
opcao = ('Celsius', 'Fahrenheit', 'Kelvin', 'Rankine', 'Réaumur')
msnOpcao = '''
[0] Celsius
[1] Fahrenheit
[2] Kelvin
[3] Rankine
[4] Réaumur
'''
msnOpcao1 = '''
A temperatura digitada está em:'''
msnOpcao2 = '''
Você irá converter para:'''

#Entrada do valor. Usuário digita a temperatura.
while True:
    try:
        temperatura = (input(msnValor))
        temperatura = temperatura.replace(',', '.')
        temperatura = float(temperatura)
        break
    except:
        print(msnInvalido)

#Escolha da opção. Usuário informa qual é a escala termométrica de entrada.
while True:
    try:
        opcaoEntrada = int(input('{} {}' .format(msnOpcao1, msnOpcao)))
        if opcaoEntrada >= 0 and opcaoEntrada <= 4:
            break
        else:
            print(msnOpcaoInvalida)
    except:
        print(msnOpcaoInvalida)

#Escolha da opção. Usuário informa qual é a escala termométrica de saída.
while True:
    print('{}' .format(msnOpcao2), end = '')
    try:
        opcaoSaida = int(input(msnOpcao))
        if opcaoSaida < 0 or opcaoSaida > 4:
            print(msnOpcaoInvalida)
        else:
            break
    except:
        print(msnOpcaoInvalida)

match opcaoEntrada:
    case 0:
        if opcaoSaida == 1:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[0], temperatura, opcao[1], conversor.celsiusFahrenheit(temperatura)))
        elif opcaoSaida == 2:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[0], temperatura, opcao[2], conversor.celsiusKelvin(temperatura)))
        elif opcaoSaida == 3:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[0], temperatura, opcao[3], conversor.celsiusRankine(temperatura)))
        elif opcaoSaida == 4:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[0], temperatura, opcao[4], conversor.celsiusReaumur(temperatura)))
        else:
            print('Não houve conversão')
    case 1:
        if opcaoSaida == 0:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[1], temperatura, opcao[0], conversor.fahrenheitCelsius(temperatura)))
        elif opcaoSaida == 2:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[1], temperatura, opcao[2], conversor.fahrenheitKelvin(temperatura)))
        elif opcaoSaida == 3:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[1], temperatura, opcao[3], conversor.fahrenheitRankine(temperatura)))
        elif opcaoSaida == 4:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[1], temperatura, opcao[4], conversor.fahrenheitReaumur(temperatura)))
        else:
            print('Não houve conversão')
    case 2:
        if opcaoSaida == 0:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[2], temperatura, opcao[0], conversor.kelvinCelsius(temperatura)))
        elif opcaoSaida == 1:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[2], temperatura, opcao[1], conversor.kelvinFahrenheit(temperatura)))
        elif opcaoSaida == 3:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[2], temperatura, opcao[3], conversor.kelvinRankine(temperatura)))
        elif opcaoSaida == 4:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[2], temperatura, opcao[4], conversor.kelvinReaumur(temperatura)))
        else:
            print('Não houve conversão')
    case 3:
        if opcaoSaida == 0:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[3], temperatura, opcao[0], conversor.rankineCelsius(temperatura)))
        elif opcaoSaida == 1:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[3], temperatura, opcao[1], conversor.rankineFahrenheit(temperatura)))
        elif opcaoSaida == 2:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[3], temperatura, opcao[2], conversor.rankineKelvin(temperatura)))
        elif opcaoSaida == 4:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[3], temperatura, opcao[4], conversor.rankineReaumur(temperatura)))
        else:
            print('Não houve conversão')
    case 4:
        if opcaoSaida == 0:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[4], temperatura, opcao[0], conversor.reaumurCelsius(temperatura)))
        elif opcaoSaida == 1:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[4], temperatura, opcao[1], conversor.reaumurFahrenheit(temperatura)))
        elif opcaoSaida == 2:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[4], temperatura, opcao[2], conversor.reaumurKelvin(temperatura)))
        elif opcaoSaida == 3:
            print('{}: {:.2f}\n{}: {:.2f}' .format(opcao[4], temperatura, opcao[3], conversor.reaumurRankine(temperatura)))
        else:
            print('Não houve conversão')