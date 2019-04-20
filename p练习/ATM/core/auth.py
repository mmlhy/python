from core import db_handler
from conf import settings
import os
import json
import time
def login_required(func):
    """
    验证是否登陆
    :param func:
    :return:
    """
    def wrapper(*args,**kwargs):
        print('--wrapper->',*args,**kwargs)
        if args[0].get('is_logined'):
            return func(*args,**kwargs)
        else:
            exit("")
    return wrapper

def save(user_data):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json"%(db_path,user_data["id"])
    with open(account_file, 'w') as f:
        f.write(json.dumps(user_data))

def acc_auth(account, password):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json"%(db_path,account)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if exp_time_stamp < time.time():
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else:
                    return account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)

def acc_login(acc_login):
    login_count = 0
    while acc_login["is_logined"] == False and login_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account, password)
        if auth:
            acc_login["is_logined"] = True
            acc_login["user_id"] = account
            return auth
        login_count += 1
    print("\033[31;1mError!!\033[0m")
    exit()

