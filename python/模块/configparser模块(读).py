import  configparser

conf = configparser.ConfigParser()
conf.read("configtest.conf")


print(conf.defaults())
print(conf["topsecret.server.com"]["Port"])

#delete
# sec = conf.remove_section('topsecret.server.com')
# conf.write(open("configtest.conf",'w'))

#改
conf.set("topsecret.server.com","Port","50")
conf.write(open("configtest.conf",'w'))
#add

conf.add_section("adc")
conf.write(open("configtest.conf",'w'))