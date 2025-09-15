from random import randint

while True:
    operador = randint(1, 1000)
    print("O operador é:", operador)

    operacao = randint(1, 5)

    operando = randint(1, 1000)
    print("O operando é:", operando)

    if operacao == 1:
        resultado = operador + operando
        print("A operacao é soma")
    elif operacao == 2:
        resultado = operador - operando
        print("A operacao é subtracao")
    elif operacao == 3:
        resultado = operador * operando
        print("A operacao é multiplicacao")
    elif operacao == 4:
        resultado = operador / operando
        print("A operacao é divisao")

    print("Qual o resultado?")

    entrada = input()

    if entrada == str(resultado):
        print("Parabéns!")
    else:
        print("Seu bocó, a resposta era:", resultado)
