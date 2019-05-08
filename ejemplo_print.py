# esto es un ejemplo de comentario
# otro comentario


"""
esto es otro comentario
de multiple lineas
"""


# ejercicio
"""
escribir un texto que se muestre en pantalla de 3 lineas 
"""


print ('hola, me llamo majo')
print ('Mi gato se llama osvaldo')
print ('trabajo en llbean')


print ('hola \nme llamo majo \npppp')

# id es el primer numero, algo de python investigar **

print("- Lista con 4 números:")
a=[57,45,7,13] # una lista con cuatro números
print(a)

# la función `len` me da la longitud de la lista
print("- Longitud de la lista:")
n=len(a)
print(n)

"""


#por último, le podés agregar elementos a una lista con el método `append`
print("- Una lista con 3 strings:")
a=['una','lista','de']
print(a)

print("- La misma lista luego de agregarle un string más:")
a.append('strings')
print(a)
"""

"""

#crear una lista de 4 numeros

mi_lista = [4,6,8,10]
#agregar al final

mi_lista.append(5)


#agregar 2 elementos al mismo tiempo

mi_lista.extend([4,5])

print ('el contenido de la lista es: ', mi_lista)




# ejemplo de duplas

# crear una tupla de 5 elementos de tipos diferentes

mi_tupla= (6, 't','osvaldo',False)

#imprimir la tupla

print (mi_tupla)

#agregar mas elementos


mi_tupla = mi_tupla + (7 , 'c')
print(mi_tupla)

#acumular elementos

mi_tupla += (2 , 'g')

print(mi_tupla)


#subtupla
#el segundo hasta el penultimo

print(mi_tupla [1:-1])

#subtupla con salto

print ('elementos pares de la tupla',mi_tupla [::2])

#los elementos impares
print ('elementos impares de la tupla',mi_tupla [1::2])


"""
#Ejercicio
# Pasar a escala de grises el color codificado en los elementos de la lista `pixel`


"""
pixel= [0.6,0.3,0.4]
pixelsuma = sum(pixel)
tampixel = len (pixel)
total = pixelsuma / tampixel
print (total)




pixel= [0.6,0.3,0.4] # intensidades de cada canal.
#El elemento 0 es el R, el 1 el G y el 2 el B

suma = pixel [0] + pixel [1] + pixel [2]
n= len(pixel)
promedio= suma / n
print ('suma=' ,suma , 'n=1' , n, 'promedio', promedio)



#promedio usando for
p=0
for numero in pixel:
    p =+ numero
p = p / len(pixel)

print ('el promedio es', p)

"""
# definir si el pixel es blanco o negro


pixel= [0.6,0.3,0.4]
pixelsuma = sum(pixel)
tampixel = len (pixel)
total = pixelsuma / tampixel
print (total)

if total >= 0.5:
    print ('el pixel es blanco')
else:
    print ('el pixel es negro')


print("Un for de 0 a 3")
for i in range(4):
    print(i)

print("- Un for de 2 a 5:")
for j in range(2,6):
    print(j



#sacar el valor maximo de la lista


lista =[44,11,15,29,53,12,30]

maximo = 0
for i in lista
    if i > maximo
     maximo = i
     print ('el maximo es ' maximo)


