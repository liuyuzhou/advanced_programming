from xml.etree.ElementTree import parse
doc = parse('named.xml')
print(f"author is: {doc.findtext('author')}")
print(f"content is: {doc.find('content')}")
print(f"content/html is: {doc.find('content/html')}")
print(f"find content: {doc.find('content/{http://www.w3.org/1999/xhtml}html')}")
print(f"find text: {doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title')}")
print('find more:\n',doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
                   '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(f"ns find: {doc.find(ns('content/{html}html'))}")
print(f"ns text find: {doc.findtext(ns('content/{html}html/{html}head/{html}title'))}")


from xml.etree.ElementTree import iterparse
for evt, elem in iterparse('named.xml', ('end', 'start-ns', 'end-ns')):
    print(f'evt is: {evt}, elem is: {elem}')

print(f'elem: {elem}')
