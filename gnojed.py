import markdown
import os
from flask import Flask, abort, flash, redirect, Markup, render_template, url_for, request

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
@app.route("/<page>")
@app.route("/<page>/")
def show(page = "home"):
  md = markdown.Markdown(extensions = ["meta", "abbr", "footnotes", "tables"], output_format = "html5")

  # Each URL maps to the corresponding .txt file in ./content/
  page_file = "./content/%s.md" % page

  # Try to open the text file, returning a 404 upon failure
  try:
    with open(page_file, "r") as f:
      # Read the entire file, converting Markdown content to HTML
      content = f.read()
      content = Markup(md.convert(content))
      meta = md.Meta

      template = "%s.html" % page
      if not os.path.exists("/templates/%s" % template):
        template = "home.html"

      return render_template(template, **locals())
  except IOError as e:
    return abort(404)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)
