
def make_tshirt (size='L', logo='I love python', sleeve=''):
    print(f'Вы хотите заказать футболку размера \"{size}\", с надписью \"{logo}?\", c {sleeve} рукавом?')
    input_history.append(size)
    input_history.append(logo)
    return input_history


input_history = []
size1 = '50'
logo1 = 'Female Body Inspector'
answer = ''
history = make_tshirt()
active = True
while active:
    size1 = input('Какой ваш размер? ')
    logo1 = input('Какой принт сделать? ')
    sleeve = input('Короткий или длинный рукав? ')
    make_tshirt(size1, logo1, sleeve)
    answer = input('Y/N? ')
    if answer.lower() == 'y':
        print('Спасибо за заказ!')
        active = False
    elif answer.lower() == 'n':
        print('Введите желаемые данные')
    else:
        print('неверная команда, повторите ввод\n')

print(history)
# make_tshirt(size='44', logo='Hello World')
# make_tshirt(size1)

from hello import *
make_pizza(44, ('1', '2', '3'))