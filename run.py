import markdown
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)

@app.route("/")
def index():
  md = markdown.Markdown(output_format='html5')

  # Each URL maps to the corresponding .txt file in ./data/
  page_file = './data/index.md'

  # Try to open the text file, returning a 404 upon failure
  try:
    f = open(page_file, 'r')
  except IOError:
    return web.notfound()

  # Read the entire file, converting Markdown content to HTML
  content = f.read()
  content = Markup(md.convert(content))

  return render_template('index.html', **locals())

if __name__ == "__main__":
  app.run()
