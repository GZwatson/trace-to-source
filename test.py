from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return 'Flask server is running', 200

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        print('No file part')
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        print('No selected file')
        return 'No selected file', 400
    filename = secure_filename('phototest.jpg')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        file.save(file_path)
        print(f'File successfully saved to {file_path}')
        return 'File successfully uploaded', 200
    except Exception as e:
        print(f'Error saving file: {e}')
        return 'Error saving file', 500

if __name__ == '__main__':
    app.run(debug=True)
