# Criação de funções
preco = 1999.90
preco2 = 100

# Calcular 5% de imposto, guardar na variável e exibir
imposto = preco * 0.05
print(imposto)

imposto2 = preco2 * 0.05
print(imposto2)

# Criar uma função para calcular o imposto de 7% e retorna para quem pediu
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

# Usar a função
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é coma  função (7%): {imposto}")

# Calcular imposto a alíquota 7% desses 4 valores e exibir
valores = [1.99, 7.99, 68.5, 1426.8]
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

# Declarar uma função calcula_imposto_aliguota que recebe 2 parâmetros: o preço do produto e a alíquota do imposto a ser aplicada. Se a alíquota não for aplicada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

# E se agora o imposto for 10%?
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")