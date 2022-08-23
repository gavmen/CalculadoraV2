# Declaração de Variáveis
listaDeValores = []
valor = 0

# Valores de 1 a 4 para definir o tipo de cálculo
print('1 = Adição\n' '2 = Subtração\n' '3 = Multiplicação\n' '4 = Divisão\n')
tipo = input('Selecione o tipo de cálculo: ')

# Testar se o valor inserido é válido.
if tipo == '1' or tipo == '2' or tipo == '3' or tipo == '4':

    # Criando funções ========================================================

    # Dois primeiros números
    def inserirValor():
        valido = False
        while not valido:  # Caso o usuário insira um valor não-numérico, repete a solicitação
            try:
                valor = float(input('Valor = '))
                listaDeValores.append(valor)
                print(listaDeValores)
                valido = True
            except ValueError:
                print('Utilize apenas números')

    # Números Extras
    def maisNumeros():  # Perguntar se o usuário quer mais que dois números na operação
        valido = False
        while not valido:  # Caso o usuário insira um valor não-numérico, repete a solicitação
            try:
                maisNumero = input("Deseja inserir mais algum número ?: ")
                if maisNumero == 'sim' or maisNumero == 's':  # Caso queira
                    inserirValor()
                elif maisNumero == 'nao' or maisNumero == 'n':  # Caso não queira
                    valido = True
                    return False
                else:
                    print('Apenas sim ou nao')
            except ValueError:
                print('Apenas sim ou nao')
    # Funcões Contas ======================================================================

    def soma():
        print('O resultado é:', sum(listaDeValores))

    def sub():
        resultado = listaDeValores[0]
        float(resultado)
        listaDeValores.pop()
        for valor in listaDeValores:
            float(valor)
            resultado = resultado - valor
        print('O resultado é:', resultado)

    def mult():
        resultado = listaDeValores[0]
        float(resultado)
        listaDeValores.pop()
        for valor in listaDeValores:
            float(valor)
            resultado = resultado * valor
        print('O resultado é:', resultado)

    def div():
        resultado = listaDeValores[0]
        float(resultado)
        listaDeValores.pop()
        for valor in listaDeValores:
            float(valor)
            resultado = resultado / valor
        print('O resultado é:', resultado)

    inserirValor()
    inserirValor()
    maisNumeros()

    match tipo:  # Corresponde as operações aos números escolhidos no começo
        case '1':
            soma()
        case '2':
            sub()
        case '3':
            mult()
        case '4':
            div()

else:  # Se o valor inserido não for válido
    print('Utilize apenas números entre 1 a 4')
