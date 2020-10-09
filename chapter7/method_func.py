from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

bai_du = UrlTemplate('http://baidu.com/s?swd={name_list}&rsv_spt={field_list}')
for line in bai_du.open(name_list='python,java,go', field_list='1'):
    print(line.decode('utf-8'))



def url_template(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

bai_du = url_template('http://baidu.com/s?swd={name_list}&rsv_spt={field_list}')
for line in bai_du(name_list='python,java,go', field_list='1'):
    print(line.decode('utf-8'))