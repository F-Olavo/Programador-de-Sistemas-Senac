'''

Contagem de vogais e consoantes
Escreva um programa que conta o numero de vogais e consoantes em uma string

Algoritimo Checklist
-[x] Receber um texto para contar as vogais
-[ ] Percorrer o texto contando cada caractere
-[ ] Salvar a contagem de cada vogal em uma lista ou dicionario
-[ ] Mostrar o resiltado
'''

# Receber um texto para contar as vogais
texto = input('Digite o texto: ')
vogais = 0
consoantes = 0
# Percorrer o texto contando cada vogal
for caractere in texto:
    if caractere in 'aeiouAEIOU':
        vogais += 1
# Percorrer o texto contando cada consoante
    if caractere.lower() in 'bcdfghjklmnpqrstvxyz':
        consoantes += 1


print(f'O texto {texto} tem {vogais} vogais')  
print(f'O texto {texto} tem {consoantes} consoantes')