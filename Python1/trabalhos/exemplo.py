preco = int (input ("Introduza o preço do terreno: "))
lado1 = int (input ("Introduza a medida do 1º lado: "))
lado2 = int (input ("Introduza a medida do 2º lado: "))
precoMedio = int (input ("Introduza o preço médio da zona: "))
area = lado1 * lado2
precoMetro = preco / area
if (precoMetro > precoMedio):
    print (f"O preço {precoMetro} é mais caro que o preço médio de {precoMedio}")
elif (precoMetro < precoMedio):
    print (f"O preço {precoMetro} é mais barato que o preço médio de {precoMedio}")
else: 
    print (f"O preço {precoMetro} é igual ao preço médio de {precoMedio}")
