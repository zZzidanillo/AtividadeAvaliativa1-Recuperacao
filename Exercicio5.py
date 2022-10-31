n = int(input("Insira um número inteiro maior ou igual à 50: "))

if n < 50:
    print("Apenas valores maiores ou iguais à 50.")
else:
    h = 0
    s = 0
    p = 0
    valor_potenciado = 1
    numero_primo = 2
    valor_negativo_positivo = 0

    for x in range(1, n + 1):
        if x == 1 or x % 2 == 0:
            valor_negativo_positivo = 1
        else:
            valor_negativo_positivo = -1

        h = h + (x * 2 - 1) / x * valor_negativo_positivo

        if x != 1:
            valor_negativo_positivo = valor_negativo_positivo * -1

        s = s + x / (x * x * valor_negativo_positivo)

        if x != 1:
            numero_nao_eh_primo = True
            valor_potenciado += 2
            while numero_nao_eh_primo:
                numero_primo += 1
                for i in range(2, numero_primo):
                    if (numero_primo % i) == 0:
                        break
                    elif i == numero_primo - 1:
                        numero_nao_eh_primo = False

        p = p + numero_primo / (valor_potenciado ** 3)

    print("Valor de H: ", h)
    print("Valor de S: ", s)
    print("Valor de P: ", p)