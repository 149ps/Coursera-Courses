"""import xml.etree.ElementTree as ET
data='''<note>
<to head='1'>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>'''
tree=ET.fromstring(data)
print("From:",tree.find('from').text)
print("Body:",tree.find('body').text)
print("Head:",tree.find('to').get('head'))"""
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    lst1=item.split(',')   
    print("The store has {lst[1]} {lst[0]}, each of {lst[2]} USD.".format(lst=lst1))

word='parth'
print(word[-1:])