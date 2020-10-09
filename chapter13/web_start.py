import webbrowser

webbrowser.open('http://www.python.org')


webbrowser.open_new('http://www.python.org')

webbrowser.open_new_tab('http://www.python.org')


c = webbrowser.get('chrome')
c.open('http://www.python.org')
c.open_new_tab('http://docs.python.org')
