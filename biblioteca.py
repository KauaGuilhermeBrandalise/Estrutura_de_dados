import numpy as np


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Status: {status}")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livros_emprestados.append(livro)
            print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
        else:
            print(f"O livro '{livro.titulo}' não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.disponivel = True
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print(f"{self.nome} não tem o livro '{livro.titulo}' emprestado.")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []  

    def add_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def exibirlivrosdisponiveis(self):
        print("Livros disponíveis na biblioteca:")
        livros_disponiveis = [livro for livro in self.livros if livro.disponivel]
        if livros_disponiveis:
            for livro in livros_disponiveis:
                livro.detalhes()
        else:
            print("Nenhum livro disponível no momento.")

# Teste do sistema

l1 = Livro("As longas tranças de um careca", "Jhon cabeludo")
l2 = Livro("A volta dos que não foram", "Estive viajante")
l3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

# Criando a biblioteca
biblioteca = Biblioteca("Biblioteca Central")

biblioteca.add_livro(l1)
biblioteca.add_livro(l2)
biblioteca.add_livro(l3)

biblioteca.exibirlivrosdisponiveis()

usuario1 = Usuario("Kauã")

usuario1.emprestar_livro(l1)

biblioteca.exibirlivrosdisponiveis()

usuario1.devolver_livro(l1)

biblioteca.exibirlivrosdisponiveis()
