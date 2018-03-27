from flask import Flask, request, json, render_template
import os
import uuid

app = Flask(__name__)
base_path = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(base_path, "static\\USER_IMAGE", f_name))
        return json.dumps({'filename': f_name})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
