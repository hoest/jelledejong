import markdown
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)

@app.route("/")
@app.route("/<page>")
def show(page = "index"):
  md = markdown.Markdown(output_format="html5")

  # Each URL maps to the corresponding .txt file in ./data/
  page_file = "./data/%s.md" % page

  # Try to open the text file, returning a 404 upon failure
  try:
    with open(page_file, "r") as f:
      # Read the entire file, converting Markdown content to HTML
      content = f.read()
      content = Markup(md.convert(content))

      return render_template("index.html", **locals())
  except IOError as e:
    return web.notfound()

if __name__ == "__main__":
  app.run(host = "0.0.0.0")
