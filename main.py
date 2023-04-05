from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html", title="Главная")
    

def main():
    app.run(port=5005)


if __name__ == '__main__':
    main()
