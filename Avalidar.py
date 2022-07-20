import CNPJValid

t = input('Digite seu CNPJ para ser validado: ')


if CNPJValid.valida(t):
    print(f'{t} É valido =)')
else:
    print(f'{t} É invalido :/')