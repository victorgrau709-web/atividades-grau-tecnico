
area = float(input("Digite o tamanho da área a ser pintada (em m²): "))


cobertura_por_litro = 3
litros_por_lata = 18
preco_lata = 80.00

litros_necessarios = area / cobertura_por_litro


quantidade_latas = math.ceil(litros_necessarios / litros_por_lata)


preco_total = quantidade_latas * preco_lata

# Exibe os resultados
print(f"\nQuantidade de latas a serem compradas: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")
