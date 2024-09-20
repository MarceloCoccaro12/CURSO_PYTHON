"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutávei (NÃO PODE MUDAR O VALOR) que vimos: str, int, float, bool
"""
string = "1000"
outra_variavel = f'{string[:3]}ABC{string[4:]}'
#print(string)
#print(outra_variavel)
print(string.zfill(10))
