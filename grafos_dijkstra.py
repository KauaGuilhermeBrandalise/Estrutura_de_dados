import heapq

class Grafo:
    def __init__(self):
        self.dicionario = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.dicionario:
            self.dicionario[vertice] = []
        else:
            print(f"Vertice {vertice} já existe.")

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.dicionario and vertice2 in self.dicionario:
            self.dicionario[vertice1].append((vertice2, peso))
            self.dicionario[vertice2].append((vertice1, peso))  

    def dijkstra(self, origem):
        distancias = {vertice: float('inf') for vertice in self.dicionario}
        distancias[origem] = 0
        prioridade = [(0, origem)]  
        visitados = set()

        while prioridade:
            distancia_atual, vertice_atual = heapq.heappop(prioridade)

            if vertice_atual in visitados:
                continue
            visitados.add(vertice_atual)

            for vizinho, peso in self.dicionario[vertice_atual]:
                distancia = distancia_atual + peso

                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(prioridade, (distancia, vizinho))

        return distancias

    def mostrar_grafo(self):
        for vertice, arestas in self.dicionario.items():
            print(f"{vertice} -> {', '.join(f'{vizinho}({peso})' for vizinho, peso in arestas)}")


grafo = Grafo()
grafo.adicionar_vertice("Nizhny Novgorod")#0
grafo.adicionar_vertice("Kazan")#1
grafo.adicionar_vertice("São Petersburgo")#2
grafo.adicionar_vertice("Moscou")#3
grafo.adicionar_vertice("Ecaterimburgo")#4
grafo.adicionar_vertice("Novosbirsk")#5
grafo.adicionar_vertice("Omsk")#6
grafo.adicionar_vertice("Samara")#7
grafo.adicionar_vertice("Arrangua")#8
grafo.adicionar_aresta("Nizhny Novgorod", "Kazan", 2)
grafo.adicionar_aresta("Nizhny Novgorod", "São Petersburgo", 7)
grafo.adicionar_aresta("Nizhny Novgorod", "Novosbirsk", 6)
grafo.adicionar_aresta("São Petersburgo", "Novosbirsk", 1)
grafo.adicionar_aresta("Novosbirsk", "Ecaterimburgo", 2)
grafo.adicionar_aresta("Ecaterimburgo", "Omsk", 10)
grafo.adicionar_aresta("Omsk", "Samara", 9)
grafo.adicionar_aresta("Samara", "Ecaterimburgo", 14)
grafo.adicionar_aresta("Kazan", "Ecaterimburgo", 4)
grafo.adicionar_aresta("Kazan", "Arrangua", 8)
grafo.adicionar_aresta("Kazan", "Samara", 7)
grafo.adicionar_aresta("Arrangua", "Moscou", 4)
grafo.adicionar_aresta("Moscou", "São Petersburgo", 8)
grafo.adicionar_aresta("São Petersburgo", "Arrangua", 11)

grafo.mostrar_grafo()
distancias = grafo.dijkstra("Nizhny Novgorod")#0
print("\nDistâncias mínimas a partir da cidade Nizhny Novgorod:")#0
for vertice, distancia in distancias.items():
    print(f"{vertice}: {distancia}")