import markdown
import os

TOP_TEMPLATING = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Max Francis - Cybersecurity</title>
</head>
<body>
    <h1>Max Francis - Cybersecurity</h1>
    <hr>
    <nav>
        <button onclick="location.pathname='/index.html'" type="button">Blog</button>
        <button onclick="location.pathname='/about.html'" type="button">About</button>
    </nav>"""

INDEX_TOP_TEMPLATING = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Max Francis - Cybersecurity</title>
</head>

<body>
    <h1>Max Francis - Cybersecurity</h1>
</body>
<hr>
<nav>
    <button onclick="location.pathname='/index.html'" type="button">Blog</button>
    <button onclick="location.pathname='/about.html'" type="button">About</button>
</nav>
<hr>

<h2>- Blog Posts -</h2>
<h3> 2022 </h3>
<ul>
    <li><a href="https://blog.maxfrancis.me/posts/simple_is_better.html">Simple is Better - 1st December 2022</a></li>
</ul>
<h3> 2021 </h3>
<ul>
    <li><a href="https://blog.maxfrancis.me/posts/hello_world.html">Here we go Again - 11th November 2021</a></li>
</ul>

<hr>
<footer>Max Francis - CC By Attribution</footer>

</html>
"""

BOTTOM_TEMPLATING = """</body>
<hr>
<footer>Max Francis - CC By Attribution</footer>

</html>"""

if __name__ == '__main__':

    article_names = []

    file_path = os.path.dirname(__file__)
    os.chdir(file_path)
    for filename in os.listdir('../_posts'):
        f = os.path.join('../_posts/', filename)
        with open(f, 'r', encoding="utf8") as f:
            article_names.append(filename)
            text = f.read()
            html = markdown.markdown(text)

        filename = filename.replace('.md', '.html')

        # make a directory for the exported HTML files if it doesn't exist
        if not os.path.exists('../_export'):
            os.makedirs('../_export')

        with open('../_export/'+filename, 'w', encoding="utf8") as f:
            f.write(TOP_TEMPLATING)
            f.write(html)
            f.write(BOTTOM_TEMPLATING)
            f.close()

    article_names.sort(reverse=True)
    with open('../_export/index.html', 'w') as index:
        index.write(TOP_TEMPLATING)
        index.write("""<h2>- Blog Posts -</h2>
                       <hr>""")

        year = 9999
        for article in article_names:
            print(article)
            if year > int(article[:4]):
                index.write("<h3> "+article[:4]+" </h3>")
                year = int(article[:4])

            index.write("""<li>
                <a href="https://blog.maxfrancis.me/posts/"""+article+"""">"""+article[11:-3]+""" - """+article[8:10]+""" / """+article[5:7]+""" / """+article[:4]+"""</a>
            </li>""")
        index.write(BOTTOM_TEMPLATING)
        index.close()

    for name in article_names:
        print(name)
