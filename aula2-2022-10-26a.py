# comando input(): quero permitir que 
# o usuário digite algo...
nome = input("Digite seu nome: ")

# pede a idade para o usuário "Qual sua idade?"
idade = int(input("Digite sua idade: "))


# comando de saída - exibir na tela
print(f"Boa noite! Seu nome é {nome}")

# exibir "Sua idade é "
print("Sua idade é {}".format(idade))

# mostrar o dobro da idade 
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

# Estrutura condicional - IF
# Mostrar se a pessoa já é maior de idade!
# Os : são necessários para rodar a condição!
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir!")
else:
  print("Você é jovem, ainda...")

# E se eu quiser perguntar o gênero? (M = masculino - F = Feminino)
# Mostrar (...e você também precisa/precisou prestar o serviço militar obrigatório.)

genero = input("Informe o gênero M = masculino, F = feminino, O = Outros:")
if idade >= 18 and genero == "M":
  print("...e você também precisa/precisou prestar o serviço militar obrigatório.")
  
print("FIM!")