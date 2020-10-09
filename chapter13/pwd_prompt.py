import getpass

user = getpass.getuser()
passwd = getpass.getpass()

# for show the use of getpass
def svc_login(user, passwd):
    return True

if svc_login(user, passwd):
   print('Success!')
else:
   print('Fail!')


user = input('Enter your username: ')