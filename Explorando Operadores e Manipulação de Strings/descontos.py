# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom == 'DESCONTO10':
    preco = preco - (preco * descontos["DESCONTO10"])
elif cupom == 'DESCONTO20':
    preco = preco - (preco * descontos["DESCONTO20"])
elif cupom == 'SEM_DESCONTO':
    preco = preco

print(f'{preco:.2f}')