from random import randint

rodadas = 10
placar = 0

while rodadas > 0:
    print("Rodada:", rodadas)
    operador = randint(1, 1000)
    print("O operador é:", operador)

    operacao = randint(1, 4)

    operando = randint(1, 1000)
    if operacao == 4:
        while operador % operando != 0:
            operando = randint(1, 1000)
    print("O operando é:", operando)

    if operacao == 1:
        resultado = operador + operando
        print("A operacao é soma")
        pontos = 10
    elif operacao == 2:
        resultado = operador - operando
        print("A operacao é subtracao")
        pontos = 20
    elif operacao == 3:
        resultado = operador * operando
        print("A operacao é multiplicacao")
        pontos = 40
    elif operacao == 4:
        resultado = int(operador / operando)
        print("A operacao é divisao")
        pontos = 50
    
    print("Qual o resultado?")

    entrada = input()


    if entrada == str(resultado):
        print("Parabéns!")
        placar += pontos
    else:
        print("Seu bocó, a resposta era:", resultado)
        placar -= pontos
    print("Placar:", placar)

    print("----------")
    
    rodadas -= 1