'''
criação: crie um dicionario chamado alunos contendo 3 alunos como chaves e seus respectivos dicionarios com nome, idade e curso.
'''

aluno1 = { 
    "nome" : "Olavo",
    "idade" : 25,
    "curso" : "programador de Sistemas"
}

for chave, valor in alunos.items():
    print(f"Chave: {chave} - Dados: {valor}")