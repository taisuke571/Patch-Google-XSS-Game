
from flask import Flask, request, render_template_string, make_response
import base64
import os

app = Flask(__name__)

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script nonce="random-value" src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="/static/logos/level1.png">
      <div>
"""

page_footer = """
    </div>
  </body>
</html>
"""

main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""


@app.route('/', methods=['GET'])
def main_page():
    # Generate a nonce for each request
  

    query = request.args.get('query')

    if not query:
        content = render_template_string(page_header + main_page_markup + page_footer)
    else:
        # Flask's render_template_string automatically escapes variables unless explicitly marked as safe
        message = f"Sorry, no results were found for <b>{query}</b>. <a href='?'>Try again</a>."
        content = render_template_string(page_header + message + page_footer)

    response = make_response(content)
    
    # Set up the CSP header with 'strict-dynamic' and the nonce
    csp_policy = f"default-src 'self'; script-src 'self' 'nonce-random-value' 'strict-dynamic'; img-src 'self';"
    response.headers['Content-Security-Policy'] = csp_policy

    return response

if __name__ == "__main__":
    app.run(debug=True)

