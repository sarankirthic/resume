from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/helloworld')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/')
def serve_resume():
    resume_path = 'pdf/sarankirthic.pdf'
    return send_file(resume_path, mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug=True)
