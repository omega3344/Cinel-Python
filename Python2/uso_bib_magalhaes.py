nome = input("Como se chama? ")
num = int(input("Insira valor positivo"))
'''
import magalhaes

fatorial = magalhaes.fat(num)
print(f"{nome}, o fatorial de {num} é {fatorial}")
print(magalhaes.quad(num))
print(magalhaes.cub(num))
'''

from magalhaes import cub, quad
print(quad(num))
print(cub(num))
