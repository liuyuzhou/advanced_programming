from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    element = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        element.append(child)
    return element


course_dict = {'course_name': 'python', 'total_class': 30, 'score':0.3}
elem = dict_to_xml('course', course_dict)
print(f'elem is: {elem}')


from xml.etree.ElementTree import tostring
print(f'elem to sting is: {tostring(elem)}')


elem.set('_id','1234')
print(f'elem to sting is: {tostring(elem)}')


def dict_to_xml_str(tag, d):
    part_list = [f'<{tag}>']
    for key, val in d.items():
        part_list.append(f'<{key}>{val}</{key}>')
    part_list.append(f'</{tag}>')
    return ''.join(part_list)


d = {'courese_name': '<python>'}
print(f"dict to xml str: {dict_to_xml_str('item',d)}")
elem = dict_to_xml('item',d)
print(f'elem to sting is: {tostring(elem)}')


from xml.sax.saxutils import escape, unescape
print(f"escape: {escape('<python>')}")
print(f"unescape: {unescape('_')}")
