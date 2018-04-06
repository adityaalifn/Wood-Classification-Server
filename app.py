from flask import Flask, request, json, render_template
import os
import uuid
import predict
import image_operation

app = Flask(__name__)
APP_ROOT = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, "static/USER_IMAGE")

        if not os.path.isdir(target):
            os.mkdir(target)

        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save("./static/USER_IMAGE/"+f_name)
        result = predict.predict_class("./static/USER_IMAGE/"+f_name)
        return json.dumps({'filename': f_name, 'result': result})


def main():
    app.run()


if __name__ == '__main__':
    main()
