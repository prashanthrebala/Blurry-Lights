from flask import Flask, render_template
from code_to_name import name_from_url

app = Flask(__name__)


@app.route('/3120234xd', methods=['GET'])
def better_luck_next_time():
    return render_template("better_luck.html")


@app.route('/<code>', methods=['GET'])
def hello_world(code):
    try:
        return render_template("invite.html", name=name_from_url[code])
    except KeyError:
        return "<h1> Invalid invite ID: <code>{0}</code></h1>".format(code)


if __name__ == '__main__':
    app.run()
