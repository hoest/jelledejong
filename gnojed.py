import markdown
import os.path
import datetime

from flask import abort
from flask import flash
from flask import Flask
from flask import Markup
from flask import redirect
from flask import render_template
from flask import request
from flask import make_response
from flask import url_for

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

      # set last-modified header
      response = make_response(render_template(template, **locals()))
      lastModified = os.path.getmtime(page_file)
      lastModifiedUtc = datetime.datetime.utcfromtimestamp(lastModified)
      response.headers.add("Last-Modified", lastModifiedUtc.strftime("%a, %d %b %Y %H:%M:%S GMT"))

      return response;
  except IOError as e:
    return abort(404)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)
