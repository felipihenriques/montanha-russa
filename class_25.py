print("Montanha Russa\n")
print("Responda a pergunta!")


user_altura = int(input("Qual a sua altura? Cm: "))

bill = 0

if user_altura >= 120:
    user_idade = int(input(("Qual a sua idade? ")))
    if user_idade < 12:
        bill = 5
        print(f"Você pagou R$ {bill},00 reais")
    elif user_idade <= 17:
        bill = 7
        print(f"Você pagou R$ {bill},00 reais")
    else:
        bill = 12
        print(f"Você pagou R$ {bill},00 reais")

    user_foto = str(input("Você quer levar a foto de recodação [S/N]?  "))
    if user_foto == "S" or user_foto == "s":
        bill += 3
        print(f"Valor total pago foi R$ {bill},00")
    else:
        print(f"Valor total pago foi R$ {bill},00")

    #     if user_idade < 12:
    #         print(f'Total a pagar vai ser R$ {valorTicket_1 + taxaFoto},00')
    #     elif user_idade <= 17:
    #         print(f"Total a pagar R$ {valorTicket_2 + taxaFoto},00") 
    #     else: 
    #         print(f"Total a pagar R$ {valorTicket_3 + taxaFoto},00")

    # elif user_idade < 12:
    #     print(f"Você pagou {valorTicket_1} reais")
    # elif user_idade <= 17:
    #     print(f"Você pagou R$ {valorTicket_2} reais")
    # else:
    #     print(f"Você pagou R$ {valorTicket_3} reais")
else:
    print("Você tem menos de 120cm, então, não pode andar neste brinquedo.")

    