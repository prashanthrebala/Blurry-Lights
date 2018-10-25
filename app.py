from flask import Flask, render_template
from code_to_name import name_from_url

app = Flask(__name__)


@app.route('/<code>')
def hello_world(code):
    return render_template("invite.html", name=name_from_url[code])


if __name__ == '__main__':
    app.run()
