
users = ['Ann', 'Maria', 'Peter', 'admin', 'Kisimyaka']
users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello fellow friend! You are most welcome here!')
        else:
            print(f'Greetings {user}! Take a seat')
else:
    print('Nobody came :(')