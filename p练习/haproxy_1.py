def search(website):
    result_list = []
    search_flag = False
    with open('haproxy','r',encoding='utf-8') as f:
        for line in f:
            if 'backend {}'.format(website) in line.strip():
                search_flag = True
            if line.strip().startswith('backend') and line.strip() != 'backend {}'.format(website):
                search_flag = False
            if search_flag:
                result_list.append(line.strip())
        print(result_list)
    if result_list == []:
        print("为空，不存在")
    else:
        return result_list

def add(website):
    arg = eval(website)
    backend_title = "backend {}".format(arg['backend'])
    record_title = arg["record"]
    context_record = "server {0} weight {1} maxconn {2}".\
        format(record_title['server'],record_title['weight'],record_title['maxconn'])
    add_flag = True
    with open('haproxy', 'r+', encoding='utf-8') as f:
        for line in f:
            if line.strip() == backend_title:
                print("网址已存在!")
                add_flag = False
                break
        if add_flag:
            f.write('\n{}'.format(backend_title))
            f.write('\n\t\t{}\n'.format(context_record))

def delete(website):
    delete_flag = False
    d_flag =False
    with open('haproxy', 'r', encoding='utf-8') as f, \
        open('haproxy_bak', 'w') as f1:
        for line in f:
            if 'backend {}'.format(website) == line.strip():
                delete_flag = True
                d_flag = True
                #continue
            if line.strip().startswith('backend') and line.strip() != 'backend {}'.format(website):
                delete_flag = False
            if not delete_flag:
                f1.write(line)
    if d_flag == False:
        print("输入网址不存在")

    with open('haproxy', 'w', encoding='utf-8') as f, \
            open('haproxy_bak', 'r') as f1:
        for line in f1:
            f.write(line)

def update(website):
    update_flag = False
    update_re = False
    arg = eval(website)
    backend_title = "backend {}".format(arg['backend'])
    record_title = arg["record"]
    context_record = "server {0} weight {1} maxconn {2}". \
        format(record_title['server'], record_title['weight'], record_title['maxconn'])
    with open('haproxy', 'r', encoding='utf-8') as f, \
        open('haproxy_bak', 'w') as f1:
        for line in f:
            if line.strip() == backend_title:
                update_flag = True
            if line.strip().startswith('backend') and line.strip() != backend_title:
                update_flag =False
            if not update_flag:
                f1.write(line)
            if update_flag and not update_re:
                f1.write('\n{}'.format(backend_title))
                f1.write('\n\t\t{}\n'.format(context_record))
                update_re =True

    with open('haproxy', 'w', encoding='utf-8') as f, \
            open('haproxy_bak', 'r') as f1:
        for line in f1:
            f.write(line)


while True:
    print("请选择".center(20,"*"),
          "\n1.查\n"
          "2.增\n"
          "3.删\n"
          "4.改\n"
          "q.退出\n")
    op_haproxy = input("选择要进入模式的ID：")
    if op_haproxy == '1':
        website = input("请输入要查询的网址：例如：www.oldboy.org\n")
        search(website)
    elif op_haproxy == '2':
        website = input("请输入要新增的网址配置："
                      "例如：{'backend': 'www.baidu.com','record': {'server': '100.1.7.8',"
            "'weight': 20,'maxconn': 3000}}\n")
        add(website)
    elif op_haproxy == '3':
        website = input("请输入要删除的网址配置："
                         "例如：www.baidu.com\n")
        delete(website)
    elif op_haproxy =='4':
        website = input("请输入要修改的网址配置："
                         "例如：{'backend': 'www.baidu.com','record': {'server': '100.1.7.8',"
                "'weight': 20,'maxconn': 3000}}\n")
        update(website)
    elif op_haproxy == 'q':
        break
    else:
        print("请检查您的输入！")
