# # # Desafio 1: Contando Caracteres

# # # Solicita que o usuário digite uma frase e armazena a entrada na variável 'digite_uma_frase'
# # digite_uma_frase = str(input("Digite uma frase: "))

# # # Remove todos os espaços da frase usando o método .replace()
# # # Substitui cada espaço (' ') por uma string vazia ('')
# # nova_frase = digite_uma_frase.replace(' ', '')

# # # Conta quantos caracteres existem na nova frase (sem espaços)
# # quantidades_de_letras = len(nova_frase)

# # # Exibe a frase sem espaços
# # print(f"A frase sem espaços é {nova_frase}")

# # # Exibe a quantidade de letras (caracteres) da frase sem espaços
# # print(f"A quantidade de letras é {quantidades_de_letras}")




# # # Desafio 2: Todas as letras maiúsculas

# # # Solicita que o usuário digite um texto e armazena a entrada na variável 'texto'
# # texto = str(input("Digite um texto: "))

# # # Converte todo o texto digitado para letras maiúsculas usando o método .upper()
# # texto_maiusculo = texto.upper()

# # # Exibe o texto convertido para maiúsculo
# # print(f"O texto em maiúsculo é: {texto_maiusculo}")




# # # Desafio 3: Verificando Palíndromos

# # # Solicita que o usuário digite uma palavra e armazena na variável 'texto'
# # texto = str(input("Digite uma palavra: "))

# # # Converte a palavra digitada para letras minúsculas, facilitando a comparação (ignora maiúsculas/minúsculas)
# # texto_formatado = texto.lower()

# # # Verifica se a palavra é igual a ela mesma escrita de trás pra frente
# # # texto_formatado[::-1] inverte a string
# # if (texto_formatado == texto_formatado[::-1]):
# #     # Se for igual, é um palíndromo
# #     print(f"A palavra '{texto}' é um palíndromo")
# # else:
# #     # Caso contrário, não é um palíndromo
# #     print(f"A palavra '{texto}' não é um palíndromo")




# # # Desafio 4: Contador de Vogais

# # # Solicita que o usuário digite um caractere (ou texto) e armazena na variável 'caracter'
# # caracter = str(input("Digite um caractere: "))

# # # Converte o texto digitado para letras minúsculas, facilitando a comparação
# # caracter_formatado = caracter.lower()

# # # Inicializa o contador de vogais com o valor 0
# # contador_vogais = 0

# # # Percorre cada letra (ou caractere) na string digitada
# # for caracter in caracter_formatado:
# #     # Verifica se o caractere atual é uma vogal
# #     if caracter in 'aeiou':
# #         # Se for vogal, incrementa o contador
# #         contador_vogais += 1

# # # Exibe o número de vezes que uma vogal apareceu na entrada
# # print(f"O caractere aparece {contador_vogais} vezes.")




# # # Desafio 5: Substituindo palavras 

# # # Solicita que o usuário digite uma frase completa
# # texto = str(input("Digite uma frase: "))

# # # Solicita a palavra que o usuário deseja substituir dentro da frase
# # texto_Substituada = str(input("Digite uma palavra que deseja substituir: "))

# # # Solicita a nova palavra que irá substituir a anterior
# # texto_Substituada_por = str(input("Digite uma palavra para substituir: "))

# # # Substitui todas as ocorrências da palavra antiga pela nova, usando o método .replace()
# # texto_formatado = texto.replace(texto_Substituada, texto_Substituada_por)

# # # Exibe a frase original e a frase com as substituições aplicadas
# # print(f"Seu texto inical foi '{texto}' e seu texto formatado foi '{texto_formatado}'")




# # # Desafio 6: Nome formatado

# # # Solicita que o usuário digite seu nome completo e armazena na variável nome_completo
# # nome_completo = str(input("Digite seu nome completo: "))

# # # Converte o nome completo para letras maiúsculas
# # nome_completo_maiusculo = nome_completo.upper()

# # # Converte o nome completo para letras minúsculas
# # nome_completo_minusculo = nome_completo.lower()

# # # Remove todos os espaços do nome em minúsculo
# # nome_completo_sem_espacos = nome_completo_minusculo.replace(" ", "")

# # # Conta quantos caracteres tem o nome sem os espaços (ou seja, só as letras)
# # quatidade_de_letras = len(nome_completo_sem_espacos)

# # # Separa o nome completo em palavras e pega o primeiro nome (índice 0)
# # primeiro_nome = nome_completo.split()[0]

# # # Conta quantas letras tem o primeiro nome
# # lestras_do_primeiro_nome = len(primeiro_nome)

# # # Exibe os resultados para o usuário
# # print("\n=============== Resultados ================")
# # print(f"Nome em maiúsculas: {nome_completo_maiusculo}")
# # print(f"Nome em minúsculas: {nome_completo_minusculo}")
# # print(f"Número total de letras (sem espaços): {quatidade_de_letras}")
# # print(f"Primeiro nome: {primeiro_nome}")
# # print(f"Número de letras do primeiro nome: {lestras_do_primeiro_nome}")




# # # Desafio 7: Invertendo a String

# # # Solicita ao usuário que digite uma frase e armazena na variável 'texto'
# # texto = str(input("Digite uma frase: "))

# # # Inverte a string utilizando fatiamento [::-1]
# # # Isso significa: comece do final até o início, de 1 em 1 (sentido reverso)
# # texto_invertido = texto[::-1]

# # # Exibe o texto original e o texto invertido
# # print(f"Seu texto foi {texto} e o invertido fica: {texto_invertido}")


# #Desafio 8 
# frase_user = input("Digite uma frase: ")
# frase_final= input("Qual frase voce deseja verificar: ")

# frase_user= frase_user.lower()
# frase_final= frase_final.lower()

# if frase_final in frase_user :
#     print(f"a palavra presente esta correta portanto sera '{frase_final}'.")
# else:
#     print("palavra não encontrada tente novamente com oq voce colocou na frase.")

#desafio 9 
#'000.000.000-00'

# numero_cpf= str(input("digite seu CPF: "))

# cpf_final= (numero_cpf[0:3] + '.' + numero_cpf[3:6] + '.' + numero_cpf[6:9] + '-' + numero_cpf[9:11])

# print(f"{cpf_final}")

#DESAFIO 10 

# number= int(input("digite seu numero inteiro para somar entre eles: "))
# number_inteiro= str(number)

# soma= 0

# for digito in number_inteiro:
#     soma += int(digito)

# print(f"A soma dos dígitos de {number} é: {soma}")










