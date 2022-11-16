# Pedir o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostrar "{nome}, você é sabichão..."

nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))
if (nota == 10):
  print(f"{nome}, você é sabichão...")
elif (nota >= 6 and nota < 10):
  print("Bom trabalho, mas dá pra melhorar.")
else:
  print("Burro! Volte e estude mais!")