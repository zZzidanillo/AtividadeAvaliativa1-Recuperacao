ultimo_numero = 0

maior_sequencia_consecutiva = 1
quantidade_consecutiva_crescente = 1

maior_sequencia_constante = 1
quantidade_consecutiva_constante = 1

for x in range(10):
    n = int(input("Insira um número inteiro: "))
    if x != 0:
        if n == ultimo_numero + 1:
            quantidade_consecutiva_crescente += 1
            if maior_sequencia_consecutiva < quantidade_consecutiva_crescente:
                maior_sequencia_consecutiva = quantidade_consecutiva_crescente
        else:
            quantidade_consecutiva_crescente = 1

        if n == ultimo_numero:
            quantidade_consecutiva_constante += 1
            if maior_sequencia_constante < quantidade_consecutiva_constante:
                maior_sequencia_constante = quantidade_consecutiva_constante
        else:
            quantidade_consecutiva_constante = 1
    ultimo_numero = n

print("O tamanho da maior sequência consecutiva de números em ordem crescente é: ", maior_sequencia_consecutiva)
print("O tamanho da maior sequência consecutiva de números constantes é: ", maior_sequencia_constante)