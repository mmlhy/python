def if_continue():
    if_cont = input("\33[34;1mDo you want to continue to operate on files [y]/[n]:\33[0m\n")
    if if_cont == 'y':
        pass
    else:
        exit()

def info_message(options):
    print("\33[31;1mInfo of %s\33[0m".center(50,'*')%options)

with open("haproxy","a+",encoding="utf-8") as file_haproxy:
    while True:
        dict_file = {}
        file_haproxy.seek(0)
        for line in file_haproxy:
            if "backend" in line and "use_backend" not in line:
                dict_file[line.split()[1]] = file_haproxy.readline().strip()
        print("File_Operations_Backend".center(50,'*'),"\n1\tQuery\n2\tAdd\n3\tDel\nq\tQuit")
        user_choice = input("\33[34;1mSelect the ID to operate:\33[0m")

        if user_choice == '1':
            info_query = input("\33[34;1mInput information to operate:\33[0m")
            if info_query in dict_file.keys():
                info_message("Query")
                print(dict_file[info_query])

            else:
                print("\33[31;1mError:No query to the corresponding information!\33[0m")
            if_continue()

        elif user_choice == '2':
            info_add = input("\33[34;1mInput information to add：\33[0m")
            try:
                dict_add = eval(info_add)
                if dict_add["backend"] not in dict_file.keys():
                    dict_add_record = dict_add["record"]
                    file_add = "backend %s\n\t\tserver %s weight %s maxconn %s\n" %(dict_add["backend"],
                                                                                    dict_add_record["server"],
                                                                                    dict_add_recordp["weight"],
                                                                                    dict_add_record["maxconn"])
                    file_haproxy.write(file_add)
                    info_message("Add")
                    print("\33[32;1mSuccessfully adding information backed %s to a file"%(dict_add["backend"]))
                else:
                    print("\33[31;1mError:Add the information already exists!\33[0m")
                if_continue()
            except Exception:
                print("\33[31;1mError:Please enter the dict format!\33[0m")
                if_continue()
        elif user_choice == '3':
            info_del = input("\33[34;1mInput information to del:\33[0m")
            try:
                dict_del = eval(info_del)
                if dict_del["backend"] in dict_file.keys():
                    file_haproxy.seek(0)
                    list_del = file_haproxy.readlines()
                    #print(type(list_del))
                    index = list_del.index("backend %s\n" % (dict_del["backend"]))
                    del list_del[index]
                    del list_del[index]
                    file_haproxy.truncate(0)
                    for line in list_del:
                        file_haproxy.write(line)
                    info_message("Del")
                    print("\33[32;1mSuccessfully delect information backend %s to a file\33[0m" % (dict_del["backend"]))

                else:
                    print("\33[31;1mError:Delect the information is not exists!\33[0m")

                if_continue()
            except Exception:
                print("\33[31;1mError:Please enter the dict format!\33[0m")
                if_continue()

        elif user_choice == "q":
            print("\33[31;1mExit\33[0m".center(30, "-"))
            exit()
        else:
            print("\33[31;1mError:Select the ID does not exist!\33[0m")