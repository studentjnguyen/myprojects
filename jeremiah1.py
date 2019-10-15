items = ['first string', 'second string']
html_str = "<ul>\n"
for item in items:
    html_str += "<li>"+item+"<li/>\n"
html_str = html_str + "</ul>"
print(html_str)
