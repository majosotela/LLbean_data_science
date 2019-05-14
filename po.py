var_first_list = int(input("Dígame cuántas palabras tiene la primera lista: ")) #numero

if var_first_list < 1:
    print("¡Imposible!")
else:
    first_list = [] #primera = first_list
    for i in range(var_first_list):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        first_name = input()
        first_list += [first_name]
    print("La primera lista es:", first_list)

    for i in range(len(first_list)-1, -1, -1):
        if first_list[i] in first_list[:i]:
            del(first_list[i])
    # print("La primera lista sin repeticiones es:", primera)

    var_second_list = int(input("Dígame cuántas palabras tiene la segunda lista: "))

    if var_second_list < 1:
        print("¡Imposible!")
    else:
        second_list = []
        for i in range(var_second_list):
            print("Dígame la palabra", str(i + 1) + ": ", end="")
            first_name = input()
            second_list += [first_name]
        print("La segunda lista es:", second_list)

        for i in range(len(second_list)-1, -1, -1):
            if second_list[i] in second_list[:i]:
                del(second_list[i])
        # print("La segunda lista sin repeticiones es:", segunda)

        share_list = []
        for i in first_list:
            if i in second_list:
                share_list += [i]
        print("Palabras que aparecen en las dos listas:", share_list)

        only_first = []
        for i in first_list:
            if i not in second_list:
                only_first += [i]
        print("Palabras que sólo aparecen en la primera lista:", only_first)

        only_second = []
        for i in only_second:
            if i not in first_list:
                only_second += [i]
        print("Palabras que sólo aparecen en la segunda lista:", only_second)

        todas = share_list + only_first + only_second
        print("Todas las palabras:", todas)