# SEGUNDA PARTE

#EJERCICIO 1

var_1 = int(input("Inserte los nombres que desea agregar a la lista: "))

if var_1 < 1:
    print("Numero invalido")
else:
    new_list = []
    for i in range(var_1):
        print("Escriba el nombre", str(i + 1) + ": ", end="")
        new_name = input()
        new_list += [new_name]
    print("La nueva lista contiene los nombres: ", new_list)


'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, 
pida una palabra y diga cuántas veces aparece esa palabra en la lista.

'''

var_2 = int(input("Inserte los nombres que desea agregar a la lista: "))

if var_2 < 1:
    print("Numero invalido")
else:
    new_list_2 = []
    for i in range(var_2):
        print("Escriba el nombre", str(i + 1) + ": ", end="")
        new_name_2 = input()
        new_list_2 += [new_name_2]
    print("La nueva lista contiene los nombres: ", new_list_2)

    find_1 = input("Escriba el nombre que desea verificar: ")
    count_1 = 0
    for i in new_list_2:
        if i == find_1:
            count_1 += 1;
    if count_1 == 0:
        print("El nombre: '" + find_1 + "' no se encuentra en la lista.")
    elif count_1 == 1:
        print("El nombre: '" + find_1 + "' aparece 1 vez en la lista.")
    else:
        print("El nombre: '" + find_1 + "' aparece", count_1, "veces en la lista.")