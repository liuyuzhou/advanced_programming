test_str = 'Elements are written as "<tag>text</tag>".'
import html
print(test_str)

print(html.escape(test_str))

print(html.escape(test_str, quote=False))



test_str = 'Spicy Jalapeño'
print(test_str.encode('ascii', errors='xmlcharrefreplace'))


test_str = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(test_str))


text = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
unescape(text)
