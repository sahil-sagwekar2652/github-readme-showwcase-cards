from flask import Flask, request, render_template
from flask.wrappers import Response
import os

from .utils import data_uri_from_url, data_uri_from_file


app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY')

# make data_uri_from_file function globally accessible
app.jinja_env.globals.update(data_uri_from_file=data_uri_from_file)

# enable jinja2 autoescape for all files including SVG files
app.jinja_options["autoescape"] = True


@app.route('/')
def index():
    if request.args.get('username') is None:
        return render_template('index.html')
    else:
        if request.args.get('theme') == 'light':
            bg_color = '#ffff'
            text_color = '#0000'
        elif request.args.get('theme') == 'dark':
            bg_color = '#0000'
            text_color = '#ffff'

        response = Response(
            status=200,
            response=render_template(
                'card.svg',
                name=request.args.get('name'),
                username=request.args.get('username'),
                headline=request.args.get('headline'),
                resume=request.args.get('resume'),
                bg_color=bg_color,
                text_color=text_color,
                avatar=data_uri_from_url(request.args.get('avatar')),
                ),
            mimetype="image/svg+xml",
            )
        response.headers["Content-Type"] = "image/svg+xml; charset=utf-8"
        return response


if __name__ == '__main__':
    app.run(debug=True)
