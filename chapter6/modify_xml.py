from xml.etree.ElementTree import parse, Element
doc = parse('test.xml')
root = doc.getroot()
print(f'root is: {root}')
root.remove(root.find('sri'))
root.remove(root.find('cr'))
print(f"root children index: {root.getchildren().index(root.find('nm'))}")
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

print(f"doc write: {doc.write('newpred.xml', xml_declaration=True)}")
