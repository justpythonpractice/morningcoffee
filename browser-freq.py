import webbrowser
links_from_file = open('links.txt', 'r+').readlines()
for i in links_from_file:
    i = i.replace('\n', '')
    print('%r' % (i))
    webbrowser.open_new_tab(i)
