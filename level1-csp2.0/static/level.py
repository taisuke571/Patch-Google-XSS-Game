from flask import Flask, request, render_template_string, make_response

app = Flask(__name__)

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="/static/game-frame.js"></script>
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
    # Disable the reflected XSS filter for demonstration purposes
    response = make_response()
    response.headers["X-XSS-Protection"] = "0"

    if not request.args.get('query'):
        # Show main search page
        content = page_header + main_page_markup + page_footer
    else:
        query = request.args.get('query', '[empty]')
        # Our search engine broke, we found no results :-(
        message = "Sorry, no results were found for <b>" + query + "</b>."
        message += " <a href='?'>Try again</a>."
        # Display the results page
        content = page_header + message + page_footer

    response.data = content

    # Set the CSP header directly here
    csp_policy = {
        "default-src": "'self'",
        "script-src": "'self'",
        "style-src": "'self'",
        "img-src": "'self'",
        "object-src": "'none'",
        "base-uri": "'self'",
        "form-action": "'self'",
        "frame-ancestors": "'none'"
    }
    response.headers["Content-Security-Policy"] = "; ".join([f"{k} {v}" for k, v in csp_policy.items()])

    return response

if __name__ == "__main__":
    app.run(debug=True)
