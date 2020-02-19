current_users = ['Ann', 'Maria', 'Peter', 'admin', 'Kisimyaka']
new_users = ['Jeorge', 'Muke', 'Maria', 'Magdalena', 'Admin']

check_users = []
for user in current_users:
    check_users.append(user.lower())

for user in new_users:
    if user.lower() in check_users:
        print(f'Username {user} is not avaliable!')
    else:
        print(f'You can use username {user}')

