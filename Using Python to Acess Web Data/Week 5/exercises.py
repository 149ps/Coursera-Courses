import xml.etree.ElementTree as ET
data='''<note>
<to head='1'>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>'''
tree=ET.fromstring(data)
print("From:",tree.find('from').text)
print("Body:",tree.find('body').text)
print("Head:",tree.find('to').get('head'))