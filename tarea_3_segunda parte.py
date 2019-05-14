# SEGUNDA PARTE

#EJERCICIO 1

var_1 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

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

var_2 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

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


'''
3.Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
'''

var_3 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

if var_3 < 1:
    print("Numero invalido")
else:
    new_list_3 = []
    for i in range(var_3):
        print("Escriba el nombre", str(i + 1) + ": ", end="")
        new_name_3 = input()
        new_list_3 += [new_name_3]
    print("La nueva lista contiene los nombres:", new_list_3)

    find_2 = input("Sustituir el nombre: ")
    change_1 = input("por este otro nombre: ")
    for i in range(len(new_list_3)):
        if new_list_3[i] == find_2:
            new_list_3[i] = change_1
    print("La lista es ahora:", new_list_3)

'''
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida una palabra y elimine esa palabra de la lista.

'''

var_4 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

if var_4 < 1:
    print("Numero Invalido")
else:
    new_list_4 = []
    for i in range(var_4):
        print("Escriba el nombre", str(i + 1) + ": ", end="")
        new_name_4 = input()
        new_list_4 += [new_name_4]
    print("La nueva lista contiene los nombres:", new_list_4)

    delete_1 = input("Nombre que quiere eliminar: ")
    for i in range(len(new_list_4)-1, -1, -1):
        if new_list_4[i] == delete_1:
            del(new_list_4[i])
    print("La lista es ahora:", new_list_4)

'''
Escriba un programa que permita crear dos listas de palabras y que, 
a continuación, elimine de la primera lista los nombres de la segunda lista.

'''

var_5 = int(input("Inserte la cantidad de nombres que desea agregar a la lista:  "))

if var_5 < 1:
    print("Numero Invalido")
else:
    first_list = []
    for i in range(var_5):
        print("Escriba el nombre: ", str(i + 1) + ": ", end="")
        new_name_5 = input()
        first_list += [new_name_5]
    print("La nueva lista contiene los nombres::", first_list)

    second_list = int(input("Inserte la cantidad de nombres que desea eliminar de la listar: "))

    if second_list < 1:
        print("Numero invalido")
    else:
        delete_2 = []
        for i in range(second_list):
            print("Escriba el nombre", str(i + 1) + ": ", end="")
            new_name_5 = input()
            delete_2 += [new_name_5]
        print("La lista de nombres a eliminar es:", delete_2)

        for i in delete_2:
            for j in range(len(first_list)-1, -1, -1):
                if first_list[j] == i:
                    del(first_list[j])
        print("La lista es ahora:", first_list)

'''
Escriba un programa que permita crear una lista de palabras y que,
 a continuación, cree una segunda lista igual a la primera, pero al revés 
 (no se trata de escribir la lista al revés, sino de crear una lista distinta).

'''

var_6 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

if var_6 < 1:
    print("Numero Invalido")
else:
    new_list_6 = []
    for i in range(var_6):
        print("Escriba el nombre", str(i + 1) + ": ", end="")
        new_name_6 = input()
        new_list_6 += [new_name_6]
    print("La nueva lista contiene los nombres: ", new_list_6)

    inverse = []
    for i in new_list_6:
        inverse = [i] + inverse
    print("La lista inversa es:", inverse)

'''
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, elimine los elementos repetidos 
(dejando únicamente el primero de los elementos repetidos).

'''

var_7 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

if var_7 < 1:
    print("Numero Invalido")
else:
    new_list_7 = []
    for i in range(var_7):
        print("Escriba el nombre", str(i + 1) + ": ", end="")
        new_name_7 = input()
        new_list_7 += [new_name_7]
    print("La nueva lista contiene los nombres: ", new_list_7)

    for i in range(len(new_list_7)-1, -1, -1):
        if new_list_7[i] in new_list_7[:i]:
            del(new_list_7[i])
    print("La lista sin repeticiones es:", new_list_7)

'''El programa debe empezar pidiendo dos listas y eliminando los elementos repetidos, como en el ejercicio anterior.
Puesto que se van a eliminar los valores de la lista, la lista se debe recorrer indirectamente y al revés (for i in range(len(lista)-1, -1, -1)).
En cada iteración del bucle, se comprueba si el elemento se encuentra en la sublista anterior a ese elemento (desde el principio hasta el elemento anterior) y si es así, se borra.
'''

first_var_8 = int(input("Inserte la cantidad de nombres que desea agregar a la lista: "))

if first_var_8 < 1:
    print("Numero Invalido")
else:
    first_list_8 = []
    for i in range(first_var_8):
        print("Escriba el nombre: ", str(i + 1) + ": ", end="")
        name_8 = input()
        first_list_8 += [name_8]
    print("La primera lista es:", first_list_8)

    for i in range(len(first_list_8)-1, -1, -1):
        if first_list_8[i] in first_list_8[:i]:
            del(first_list_8[i])
    # print("La primera lista sin repeticiones es:", primera)

    second_var_8 = int(input("Inserte la cantidad de nombres que desea agregar a la segunda lista: : "))

    if second_var_8 < 1:
        print("Numero Invalido")
    else:
        second_name_8 = []
        for i in range(second_var_8):
            print("Escriba el nombre:", str(i + 1) + ": ", end="")
            name_8 = input()
            second_name_8 += [name_8]
        print("La segunda lista es:", second_name_8)

        for i in range(len(second_name_8)-1, -1, -1):
            if second_name_8[i] in second_name_8[:i]:
                del(second_name_8[i])
        # print("La segunda lista sin repeticiones es:", segunda)

        share_list = []
        for i in first_list_8:
            if i in second_name_8:
                share_list += [i]
        print("Nombres que aparecen en ambas listas:", share_list)

        new_first_list = []
        for i in first_list_8:
            if i not in second_name_8:
                new_first_list += [i]
        print("Nombres que sólo aparecen en la primera lista:", new_first_list)

        new_second_list = []
        for i in second_name_8:
            if i not in first_list_8:
                new_second_list += [i]
        print("Nombres que sólo aparecen en la segunda lista:", new_second_list)

        todas = share_list + new_first_list + new_second_list
        print("Todas los nombres:", todas)