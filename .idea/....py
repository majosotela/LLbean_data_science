users_List =[['group_1', 177,145,167,190,140,150,180,130],
             ['group_2', 165,176,145,189,170,189,159,190],
             ['group_3', 145,136,178,200,123,145,145,134],
             ['group_4', 201,110,187,175,156,165,156,135]
      ]


for users in users_List:
    print (users)

for users in users_List:
    maxi = max(users[1:9])
    users.append(maxi)
    print(users [0],users[9])

    users_List = [[177, 145, 167, 190, 140, 150, 180, 130],
                  [165, 176, 145, 189, 170, 189, 159, 190],
                  [145, 136, 178, 200, 123, 145, 145, 134],
                  [201, 110, 187, 175, 156, 165, 156, 135]
                  ]

    result = []
    max_height = 0
    for cur_list in users_List:
        for cur_height in cur_list:
            if cur_height > max_height:
                max_height = cur_height
                result = cur_list
    print(str(result) + ' la mayor de todas las alturas de todas las personas es: ', str(max_height))

    max_height = 0
    for i in users_List:
        if i > max_height:
            max_height = i