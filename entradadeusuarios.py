# declarar variável que vai receber a entrada pelo teclado

#entrada
aluno = input('Digite o nome do aluno:')
n1 = float (input('Digite a nota1: '))
n2 = float (input('Digite a nota 2: '))
#processamento
media = (n1 + n2)/2
#saída
print('Nome do aluno: ', aluno.upper()) #letras maiúsculas
print('Nome do aluno: ', aluno.lower()) #letras minúsculas
print('Nome do aluno: ', aluno.title()) #letras iniciais dos nomes são escritas em maíusculo

print('Nota 1: ', n1)
print('Nota 2: ' , n2)
print('Sua média final foi: ' , media)
