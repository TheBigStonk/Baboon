def create_index_html():
    # Create the index.html file
    index_html = open('_export/index.html', 'w')
    index_html.write('<DOCTYPE html>')
    index_html.write(' <html>')
    index_html.write(' <head>')
    index_html.write(' <title>My Website</title>')
    index_html.write(' </head>')
    index_html.write(' <body>')
    index_html.write(' <h1>My Website</h1>')
    index_html.write(' </body>')
    index_html.write('</html>')
    index_html.close()


create_index_html()
