# Meu primeiro projeto Python!
#
# print() = comando de saida

print("Hello World!")

# Quando quiser guardar uma String! (frase)
nome = "Eduardo Bélico"
# Quando quiser guardar um numero inteiro
idade = 29
# Exibir o nome que está dentro da variavel nome!
print(nome)
# Quando quiser exibir a frase "A minha idade é" completando com o conteúdo da variavel idade (para isso uso o str para converter! ou coloco a variável dentro da frase entre chaves com um f no começo da frase! ou abro chaves dentro da frase e depois dela coloco .format(variável)) e "O meu nome é" com a variável nome

print("A minha idade é "+str(idade))
print(f"A minha idade é {idade}")
print("A minha idade é {}".format(idade))

print("O meu nome é "+nome)

# Quando quiser exibir trocando pelas variáveis nome e idade

print("Meu nome é {} e tenho {} anos".format(nome, idade))


'''
como usar comentario em bloco!
'''