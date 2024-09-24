print("\n\nvamos comparar os tamanhos dos objetos.")


padrao = int(input("escolha um padrao: "))
print("\nvoce digitou:", padrao, "como padrao")


valor1 = int(input("\n\nagora escreva o primeiro valor: "))
print("\nvoce digitou", valor1, "como primeiro valor!")


valor2 = int(input("\n\ne por fim, escreva o segundo valor: "))
print("\nvoce digitou", valor2, "como segundo valor!")

if valor1 < padrao: 
    print("\n\no valor", valor1, "é menor que o padrao.")

elif valor1 > padrao:
    print("\n\no valor", valor1, "é maior que o padrao.")


if valor2 < padrao: 
    print("\n\no valor", valor2, "é menor que o padrao.")

elif valor2 > padrao:
    print("\n\ne o valor", valor2, "é maior que o padrao.")

else:
    print("operação invalida.")