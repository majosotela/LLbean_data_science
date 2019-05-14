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