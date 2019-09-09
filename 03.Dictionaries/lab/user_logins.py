users_dict = {}

while True:
    users = input().split(' -> ')
    if users[0] == 'login':
        break

    username = users[0]
    password = users[1]

    users_dict[username] = password

unsuccessful_logins = 0

while True:
    login_requests = input().split(' -> ')

    if login_requests[0] == 'end':
        break

    username = login_requests[0]
    password = login_requests[1]

    if username in users_dict and users_dict[username] == password:
        print(f'{username}: logged in successfully')
    else:
        unsuccessful_logins += 1
        print(f'{username}: login failed')

print(f'unsuccessful login attempts: {unsuccessful_logins}')
