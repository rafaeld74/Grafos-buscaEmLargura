# Função para ler matrizes de um arquivo de texto
def ler_matrizes(nome_arquivo):
    matrizes = []
    matriz_atual = []

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Se a linha estiver em branco, a matriz atual está completa
            if linha.strip() == '':
                if matriz_atual:
                    matrizes.append(matriz_atual)
                    matriz_atual = []
            else:
                # Divida os valores da linha e converta para int (ou outro tipo desejado)
                valores = [int(valor) for valor in linha.strip().split()]
                
                # Adicione a lista de valores à matriz atual
                matriz_atual.append(valores)

        # Adicione a última matriz se houver alguma
        if matriz_atual:
            matrizes.append(matriz_atual)

    return matrizes

# Exemplo de uso
nome_do_arquivo = 'grafo.txt'
lista_de_matrizes = ler_matrizes(nome_do_arquivo)

# Imprime as matrizes lidas
for matriz in lista_de_matrizes:
    for linha in matriz:
        print(linha)
    print()  # Linha em branco entre as matrizes
