from flask import Flask, request, json, render_template
from flask_sqlalchemy import SQLAlchemy
import os, uuid, predict, image_operation

app = Flask(__name__)
APP_ROOT = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/wood'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("upload.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(APP_ROOT, "static/USER_IMAGE", f_name))
        result = predict.predict_class("static/USER_IMAGE/"+f_name)
        return json.dumps({'filename': f_name , 'result' : result})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
