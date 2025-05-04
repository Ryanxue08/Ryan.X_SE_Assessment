#Menu which includes basic options
def main():
    while True:
        menu = input('What would you like to do (Login, Register, Quit): ').lower().strip()
        match menu:
            case 'login':
                login()
            case 'register':
                register()
            case 'quit':
                print('End Program')
                break
            case _:
                print('Invalid option. Please try again.')
            



#
def register():
    register = input('What is new username: ')
    input('What is password')




def login():
    login_username = input('What is your username: ')
    login_password = input('What is your password: ')
    for account in accounts:
        if account['username'] == login_username and account['password'] == login_password:
            print('Login successful!')
            menu2()
            return
    print('Invalid username or password.')
        

#def password():
#    password = input('What is your password: ')
#    match password:
#        case 'Ancient enimes r us' | "I'm Your Father" | 'May the Force be with you' | 'patu' | 'Yoda' | 'I Am All The Jedi' | 'May the Force be with you':
#            menu2()
#        case _:
#            print('Login unsuccessful')




def menu2():
    menu2 = input('Login Succesful, Change password?, Logout: ').lower().strip()
    match menu2:
        case 'logout':
            print('Logged out.')
            main()
        case 'change password':
            change_password()
        case _:
            print('Invalid option.')










username = ['sithLord Ancient', 'd_Vader', 'GENERALleia', 'grogu', 'there_is_no_try', 'MyRey', 'Luke']
accounts = [{'username':'sithLord', 'password':'Ancient enimes r us' }, {'username':'d_Vader' , 'password':"I'm Your Father"  }, {'username':'GENERALleia' , 'password':'May the Force be with you'  }, {'username':'grogu', 'password':'patu'  }, {'username':'there_is_no_try' , 'password':'Yoda'  }, {'username':'MyRey' , 'password':'I Am All The Jedi'  }, {'username':'Luke', 'password': 'May the Force be with you'  }]




 #           case 'change password':
 #               passchange = input('What is your new password: ')
  #          case 'logout':
  #              logout = print('user is logged out')


import csv

def load_accounts():
    try:
        with open('plain_text.txt', 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
            return []

def save_account(username, password):
    with open('plain_text.txt', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'password'])
        writer.writerow({'username': username, 'password': password})



def register():
        import csv
        
        username = input('What is your username: ')
        password = input('What is your password')

        with open('plain_text.txt', 'a') as file:
            writer = csv.DictWriter(file, fieldnames =['username', 'password'])
            writer.writerow({'username': username, 'password': password})



def change_password():
    username = input('Enter your username: ')
    new_password = input('Enter your new password: ')
    for account in accounts:
        if account['username'] == username:
            account['password'] = new_password
            print('Password changed successfully! ')
            return
    print('Username not found.')


main()






