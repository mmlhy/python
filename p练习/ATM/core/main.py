from core import auth
from core.auth import login_required
from core import transaction
user_data = {
    "user_id":None,
    "is_logined":False,
    "logined_data":None
}

def account_info(user_data):
    print(user_data["logined_data"])

@login_required
def repay(user_data):
    current_balance = """
        credit: %s
        balance: %s""" % (user_data["logined_data"]["credit"], user_data["logined_data"]["balance"])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_account = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_account) > 0 and repay_account.isdigit():
            account_data = transaction.transation_make(user_data["logined_data"],"repay",repay_account)
            print(account_data["balance"])
        if repay_account == 'b':
            back_flag = True

@login_required
def withdray(user_data):
    account_data = user_data["logined_data"]
    current_balance = """
        credit: %s
        balance: %s""" % (account_data["credit"], account_data["balance"])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdray_account = input("\033[33;1mInput withdray amount:\033[0m").strip()
        if len(withdray_account) > 0 and withdray_account.isdigit():
            account_data = transaction.transation_make(account_data, "withdray", withdray_account)
            print(account_data["balance"])
        if withdray_account == 'b':
            back_flag = True


def transfer():
    account_data = user_data["logined_data"]
    current_balance = """
            credit: %s
            balance: %s""" % (account_data["credit"], account_data["balance"])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdray_account = input("\033[33;1mInput withdray amount:\033[0m").strip()
        if len(withdray_account) > 0 and withdray_account.isdigit():
            account_data = transaction.transation_make(account_data, "withdray", withdray_account)
            print(account_data["balance"])
        if withdray_account == 'b':
            back_flag = True
def lagout(user_data):
    auth.save(user_data["logined_data"])
    exit()

def interactive(user_data):
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  退出
    \033[0m'''
    menu_dic = {
        '1':account_info,
        '2':repay,
        '3':withdray,
        '4':transfer,
        '5':lagout,
    }
    exit_flag = False
    while not exit_flag :
        print(menu)
        auth_option = input(">>>:").strip()
        if auth_option in menu_dic:
            menu_dic[auth_option](user_data)
        else:
            print("\033[31;1mNumber not in list!\033[0m")
            continue







def run():
    acc_data = auth.acc_login(user_data)
    print(acc_data)
    if user_data["is_logined"] == True:
        user_data["logined_data"] = acc_data
    interactive(user_data)
