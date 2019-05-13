"""Tarea 2
1. parte:
Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.
"""

list= [5, 6, 10, 13, 3, 4]
sumlist = sum(list)
lenghtlist = len (list)
summary = sumlist / lenghtlist
print ("El promedio de los valores dentro de la lista es de:  ",summary)

"""
Escriba un código en python que determine cual grupo de personas 
contiene la mayor de todas las alturas de todas las personas
"""

users_List =[[177,145,167,190,140,150,180,130],
             [165,176,145,189,170,189,159,190],
             [145,136,178,200,123,145,145,134],
             [201,110,187,175,156,165,156,135]
      ]
max_height = 0
for cur_list in users_List:
    for cur_height in cur_list:
        if cur_height > max_height:
            max_height = cur_height
print(str(cur_list) + ' la mayor de todas las alturas de todas las personas es: ', str(max_height))

max_height = 0
for i in users_List:
    if i > max_height:
        max_height = i

"""
me da un error pero me imprime correctamente el resultado
"""