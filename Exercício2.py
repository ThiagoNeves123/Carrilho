def calcular_nota_final(notas):
 
    if len(notas) != 6:
        print("O vetor deve conter exatamente seis posições.")
        return

    notas_testes = notas[:5]
    bonus_merito = notas[5]

    notas_testes.sort(reverse=True)


    media_tres_maiores = sum(notas_testes[:3]) / 3


    nota_final = min(10, max(0, media_tres_maiores + bonus_merito))

    print(f"A nota final de AC do aluno é: {nota_final}")


vetor_notas = []
for i in range(6):
    nota = float(input(f"Informe a nota {i + 1}: "))
    vetor_notas.append(nota)

calcular_nota_final(vetor_notas)