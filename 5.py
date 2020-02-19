user_1 = {
    'first name' : 'Ivan',
    'last name' : 'Ivanov',
    'age' : '32',
    'city' : 'Urupinsk',
    'salary' : 'dohua',
    }
user_2 = {
    'first name': 'Andrey',
    'last name': 'Grachev',
    'age': '41',
    'city': 'Zlupinsk',
    'salary': 'norm',
    }

user_3 = {
    'first name': 'Gavrila',
    'last name': 'Dubolomov',
    'age': '15',
    'city': 'Moscow',
    'salary': 'no',
    }

users = [user_1, user_2, user_3]

##### для одного пользователя
# for key, value in user_1.items():
#     print(f'User\'s {key.title()} is {value.title()}')

##### для списка пользователей
# for user in users:
#     for key, value in user.items():
#         print(f'User\'s {key.title()} is {value.title()}')
#     print()

##### в одну строку
for user in users:
    mssg = ''
    for key, value in user.items():
        if key == 'first name':
            mssg += f'User {value.title()} '
        if key == 'last name':
            mssg += f'{value.title()}, '
        if key == 'age':
            mssg += f'his age is {value}, '
        if key == 'city':
            mssg += f'he is from {value.title()}, '
        if key == 'salary':
            mssg += f'he earns {value} dollars\n'
    print(mssg)


                         