"""
Desenvolva uma função que verifique se uma palavra ou frase 
lida de trás para frente é idêntica à original, exercitando 
manipulação de strings e fatiamento (slicing)
"""

print("VERIFICADOR DE PALINDROMO")
print("=" * 15)
element = input("digite a palavra: ").lower()

#remover os espaços para evitar diferença
element_clear = element.replace(" ", "")

if element_clear == element_clear[::-1]:
    print("VOCE ESCREVEU UM PALINDROMO")
else:
    print("ISSO NÃO É UM PALINDROMO")