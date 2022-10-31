popA_paisA = 15000
popB_paisA = 15000
pop_paisB = 45000
pop_paisC = 65000
anos_A = 0
anos_B = 0

while (popA_paisA <= pop_paisB):
    popA_paisA = popA_paisA + (popA_paisA * 10)/100
    pop_paisB = pop_paisB + (pop_paisB * 5) / 100
    anos_A = anos_A + 1
print("A população do país A igualará ou ultrapassará em a população do país B em", anos_A, "anos.")

while (popB_paisA <= pop_paisC + (pop_paisC * 23)/100):
    popB_paisA = popB_paisA + (popB_paisA * 10)/100
    pop_paisC = pop_paisC + (pop_paisC * 2.5) / 100
    anos_B = anos_B + 1
print("A população do país A igualará ou ultrapassará em 23% a população do país C em", anos_B, "anos.")