def calcular_media(notas):
    if len(notas) == 4:
        soma = sum(notas)
        media = soma / 4
        print("A média é:", media)
    else:
        print("Por favor, forneça exatamente 4 notas.")

# Vetor que armazena os dados
notas_usuario = []

# Informações preenchidas pelo usuário
for i in range(4):
    nota = int(input(f"Informe a nota {i + 1}: "))
    notas_usuario.append(nota)

# Calculo da media
calcular_media(notas_usuario)