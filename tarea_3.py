import operator

# Para definir la agenda del hospital
schedule_ER = []

user_list =[(('Juan', 'Mora', 100103111,65 , 81118811, 'dolor'),
          ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta'),
          ('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'))]


schedule_ER.append(user_list)

'''
Primera pregunta:
Cuantos pacientes llegaron en total?
'''
user_count=0
for patient_count in user_list:
      for p in patient_count:
          user_count=user_count+1
print ('1.Total de personas atendidas: ', user_count)

'''
Segunda pregunta:
Cuantas personas llegaron por dolor?
'''
count = user_list.count(('dolor'))
print ("La cantidad de usuarios que llegaron con dolor son: ", count)


"""
Cuarta pregunta
Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven

"""

schedule_ER.append(user_list)

print('4.La lista ordenada desde el paciente de mayor edad al menor: ',sorted(user_list, key=operator.itemgetter(3)))




