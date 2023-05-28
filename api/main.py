from flask import Flask, request, jsonify, url_for, redirect, render_template
from flask.wrappers import Response
import os


app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY')


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
                username=request.args.get('username'),
                headline=request.args.get('headline'),
                resume=request.args.get('resume'),
                bg_color=bg_color,
                text_color=text_color,
                avatar=request.args.get('avatar'),
                ),
            mimetype="image/svg+xml",
            )
        response.headers["Content-Type"] = "image/svg+xml; charset=utf-8"
        return response


if __name__ == '__main__':
    app.run(debug=True)
