sal_fixo = float(input("Insira o salário fixo do vendedor: "))
vendas = float(input("Insira o valor das vendas: "))

if vendas <= 1500:
    sal_final = sal_fixo + (vendas * 5)/100
    print("O salário total final do vendedor é de R$", sal_final)
elif vendas > 1500:
    x = vendas - 1500  # A variável x vai guardar o valor das vendas que passou de 1500
    sal_final = sal_fixo + (1500 * 5)/100 + (x * 7)/100
    print("O salário total final do vendedor é de R$", sal_final)