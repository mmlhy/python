import xml.etree.ElementTree as ET

tree = ET.parse("haarcascade_eye.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib,i.text)

#只遍历height节点
for node in root.iter('height'):
    print(node.tag,node.text)


#修改
for node in root.iter('height'):
    node_height = int(node.text)+1
    node.text = str(node_height)
    node.set("updated","yes")

tree.write("haarcascade_eye.xml")
#delete

for cascade in root.findall('cascade'):
    rank = int(cascade.find('height').text)
    if rank > 20:
        root.remove(cascade)
tree.write('output.xml')


