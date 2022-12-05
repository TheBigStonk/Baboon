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

BOTTOM_TEMPLATING = """</body>
<hr>
<footer>Max Francis - CC By Attribution</footer>

</html>"""

if __name__ == '__main__':
    file_path = os.path.dirname(__file__)
    os.chdir(file_path)
    for filename in os.listdir('../_posts'):
        f = os.path.join('../_posts/', filename)
        if os.path.isfile(f):
            print(f)
        with open(f, 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
            print(html)

        filename = filename.replace('.md', '.html')

        with open('../_export/'+filename, 'w') as f:
            f.write(TOP_TEMPLATING)
            f.write(html)
            f.write(BOTTOM_TEMPLATING)
            f.close()
