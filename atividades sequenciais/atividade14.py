peso_total = float(input("o peso total dos peixes (em kg): "))
LIMITE = 50.0
PRECO_POR_QUILO_EXCEDENTE = 4.0
if peso_total == LIMITE:
    excesso = peso_total - LIMITE
    multa = excesso * PRECO_POR_QUILO_EXCEDENTE
print("\n--- Relatório de Pesca ---")
print(f"Peso total: {peso_total:.2f} kg")

if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print("Excesso de peso: 0.00 kg")
    print("Valor da multa: R$ 0.00 (Dentro do limite permitido!)")
