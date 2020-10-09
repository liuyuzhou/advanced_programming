from xml.etree.ElementTree import parse

doc = parse('test.xml')

# Extract and output tags of interest
for item in doc.iterfind('pre'):
    pt = item.findtext('pt')
    fd = item.findtext('fd')
    v = item.findtext('v')

    print(f'the value of pt: {pt}')
    print(f'the value of fd: {fd}')
    print(f'the value of v: {v}')


print(f'doc content: {doc}')
e = doc.find('pre')
print(f'e is: {e}')
print(f'e tag is: {e.tag}')
print(f'e text value: {e.text}')
print(f"e get attribute v is: {e.get('v')}")