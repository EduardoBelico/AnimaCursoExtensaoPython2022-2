# Aprendendo laços!
contador = 1

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador + 1 # contador += 1

# Laço for (em python for = for each)
fruta = "morango"
print(fruta)

# Lista e mostrar a terceira fruta
frutas = ["morango", "laranja", "limão"]
print(frutas[1])

# Adicionar itens à lista
frutas.append("manga")

# Quantas frutas tem na minha lista?
print(len(frutas)) # length = tamanho
print(frutas)

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo com o for:")
for fruta in frutas:
  print(fruta)

