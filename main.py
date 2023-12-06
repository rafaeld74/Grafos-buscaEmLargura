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

def imprimir_resultados_bfs(matriz_adjacencia, resultado_bfs):
    num_vertices = len(matriz_adjacencia)

    # Imprimir o grafo original
    print("Grafo Original:")
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(matriz_adjacencia[i][j], end=" ")
        print()

    # Imprimir a árvore resultante da busca em largura
    print("\nÁrvore Resultante da BFS:")
    for i, vertice in enumerate(resultado_bfs):
        if i > 0:
            pai = resultado_bfs[i-1]
            print(f"Aresta de Árvore: ({pai}, {vertice})")

    # Identificar e imprimir arestas irmão e arestas primo
    print("\nClassificação das Arestas:")
    for i in range(1, num_vertices):
        vertice_atual = resultado_bfs[i]
        pai = resultado_bfs[i - 1]
        
        # Identificar vértices irmãos
        if i < num_vertices - 1:
            proximo_vertice = resultado_bfs[i + 1]
            if matriz_adjacencia[vertice_atual][proximo_vertice] == 1:
                print(f"Aresta Irmão: ({vertice_atual}, {proximo_vertice})")

        # Identificar vértices primos
        for j in range(i + 1, num_vertices):
            outro_vertice = resultado_bfs[j]
            if matriz_adjacencia[vertice_atual][outro_vertice] == 1 and outro_vertice != pai:
                print(f"Aresta Primo: ({vertice_atual}, {outro_vertice})")
                
import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(matriz_adjacencia):
    # Criar um grafo direcionado a partir da matriz de adjacência
    G = nx.DiGraph()
    num_vertices = len(matriz_adjacencia)

    # Adicionar nós ao grafo
    G.add_nodes_from(range(num_vertices))

    # Adicionar arestas ao grafo
    for i in range(num_vertices):
        for j in range(num_vertices):
            if matriz_adjacencia[i][j] == 1:
                G.add_edge(i, j)

    # Desenhar o grafo
    pos = nx.spring_layout(G)  # Layout para organizar os nós
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=15)

    # Exibir o grafo desenhado
    plt.title("Grafo Original")
    plt.show()



from collections import deque

def bfs(matriz_adjacencia, inicio):
    num_vertices = len(matriz_adjacencia)
    
    visitados = [False] * num_vertices
    fila = deque()
    resultado_bfs = []
    
    # Marca o vértice inicial como visitado e o adiciona à fila
    visitados[inicio] = True
    fila.append(inicio)
    
    while fila:
        # Remove o vértice da frente da fila
        vertice_atual = fila.popleft()
        
        # Adiciona o vértice atual ao resultado
        resultado_bfs.append(vertice_atual)
        
        # Percorre todos os vértices adjacentes ao vértice atual
        vizinho = 0
        while vizinho < num_vertices:
            if matriz_adjacencia[vertice_atual][vizinho] == 1 and not visitados[vizinho]:
                # Marca o vizinho como visitado e o adiciona à fila
                visitados[vizinho] = True
                fila.append(vizinho)
            
            vizinho += 1
    
    return resultado_bfs

# Exemplo de uso com a primeira matriz fornecida
matriz_exemplo = [
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

vertice_inicial = 0
resultado_bfs = bfs(matriz_exemplo, vertice_inicial)

print(f"Resultado da BFS a partir do vértice {vertice_inicial}: {resultado_bfs}")

# Imprimir resultados
imprimir_resultados_bfs(matriz_exemplo, resultado_bfs)

# Chamar a função para desenhar o grafo
desenhar_grafo(matriz_exemplo)



# def busca_largura(grafo):

# Exemplo de uso
nome_do_arquivo = 'grafo.txt'
lista_de_matrizes = ler_matrizes(nome_do_arquivo)



# Imprime as matrizes lidas
#for matriz in lista_de_matrizes:
#    for linha in matriz:
#        print(linha)
#    print()  # Linha em branco entre as matrizes

