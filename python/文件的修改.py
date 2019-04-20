f = open("yesterday",'r',encoding="utf-8")
f_new = open("yesterday2",'w',encoding="utf-8")

for line in f:
    if "我年少轻狂" in line:
        line = line.replace("我年少轻狂","miao年少轻狂")
    f_new.write(line)

f.close()
f_new.close()