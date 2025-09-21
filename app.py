from flask import Flask, send_file
from waitress import serve

app = Flask(__name__)


@app.route('/helloworld')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/')
def serve_resume():
    resume_path = 'pdf/sarankirthic_V2.pdf'
    return send_file(resume_path, mimetype='application/pdf')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
    # app.run(port=8000)
