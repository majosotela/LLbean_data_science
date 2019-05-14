from operator import itemgetter, attrgetter
from collections import Counter

# Para definir la agenda del hospital
schedule_ER = []

user_list =(('Juan', 'Mora', 100103111,65 , 81118811, 'dolor'),
          ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta'),
          ('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'))


schedule_ER.append(user_list)

'''
Primera pregunta:
Cuantos pacientes llegaron en total?
'''
user_count= len(user_list)
print ('1.Total de personas atendidas: ', user_count)

'''
Segunda pregunta:
Cuantas personas llegaron por dolor?
'''
counter = 0
for user in user_list:
    if 'dolor' in user:
       counter += 1

print("2.El numero de personas que llegaron por dolor es: ", counter)
"""
Cuarta pregunta
Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven

"""
print('3.La lista de pacientes empezando por el paciente de mayor edad al menor',(sorted(user_list, key =itemgetter(3), reverse=True)))

'''
Cuantos pacientes son mayores de edad? cuantos menores?

'''

print( '4. Cuantos pacientes son mayores de edad?',len([x for x in user_list if x[3] > 18]))
print( '4. Cuantos pacientes son menores de edad?', len([x for x in user_list if x[3] < 18]))


'''Suponga que se atienden con orden de prioridad por gravedad de consulta, 
empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor. 
Ordene la lista empenzando por los que tienen mayor prioridad.

'''
print ('5. Lista de pacientes segun su prioridad,siendo esta los que tienen dolor y luego por edad: ',sorted(user_list, key=itemgetter(5,3), reverse=True))


'''
Suponga que los que tienen dolor mueren :( 
Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.

'''


print('La nueva lista de prioridad seria: ',sorted(user_list, key=itemgetter(5)),len([x for x in user_list if x[5] != 'dolor']))



print(sorted(user_list, key=itemgetter(3), reverse=True))