from flask import Flask, jsonify, request, send_file, Blueprint
from flask_cors import CORS

from joiner import joiner_pdf
from helpers.validator import validateFields

app = Flask(__name__)
CORS(app, origins=['http://localhost:4321', 'https://my-joiner-pdf.vercel.app'])

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def index():
  return jsonify({'message': 'Welcome to the PDF Joiner API', 'code': '200'})

@api.route('/join', methods=['POST'])
def join():
  try:
    validate = validateFields(request)
    if validate: return validate, 400

    files = []
    for file in request.files:
      print('file >>> ', request.files[file].filename)
      files.append(request.files[file])
    
    joined_pdf = joiner_pdf(files)

    return jsonify({'message': 'PDFs unidos exitosamente.', 'code': 200, 'base64': joined_pdf}), 200
  except Exception as e:
    print('error >>> ', e)
    return jsonify({'message': 'Ocurrió un error inesperado, por favor intente nuevamente.', 'code': 422}), 422

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
