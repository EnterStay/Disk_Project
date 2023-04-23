from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('uploads/' + file.filename)  # Сохраняем файл в папке uploads
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1", debug=True)
