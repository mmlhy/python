import time

user,password = 'alex','abc123'
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            username = input("Username:").strip()
            passwd = input("PassWord:").strip()
            if auth_type =='local':
                print('local')
            if auth_type=='ldap':
                print('ldap')
            if user == username and passwd == password:
                print("\033[32;1mWelcome to home\033[0m")
                return func(*args,**kwargs)   #*****************zhongyao
            else:
                print("\033[31;1mError\033[0m")
        return wrapper
    return out_wrapper

def index():
    print("Welcome to index page")

@auth(auth_type="local")
def home():
    print("Welcome to home page")
    return "nihao"

@auth(auth_type="ldap")
def bbs():
    print("Welcome to bbs page")

index()
home()
bbs()