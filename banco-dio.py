menu = """
-------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção que deseja: 
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    saldo = round(saldo, 2)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado: "))
        saldo += valor

        if valor > 0:
            print("R$", valor, "Foram inseridos na sua conta")
        else:
            print("Operação inválida")

    elif opcao == "s":
        if numero_saques >= limite_saques:
            print("Limite de saque diário atingido")
        else:
          saque = float(input("Insira quanto deseja sacar: "))
          if saque== 0:
              print("Não é possível sacar 0R$")
          elif saque > saldo:
            print("Saldo insuficiente")
          elif saque < 0:
            print("Operação inválida")
          else:
                saldo -= saque
                numero_saques += 1
                print("Você sacou", saque, "R$")

    elif opcao == "e":
        print("Extrato final =", saldo)

    elif opcao == "q":
        print ("Seu extrato final é", saldo, "Obrigado por acessar nosso banco!")
        break
