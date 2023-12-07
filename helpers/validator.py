from flask import jsonify

def validateFields(request):
  if not request.files:
    return jsonify({'message': 'No PDFs found, please send a valid formdata with PDFs', 'code': '400'})
  
  for file in request.files:
    if not request.files[file].filename.endswith('.pdf'):
      return jsonify({'message': 'Invalid file type, please send only PDFs', 'code': '400'})
  
  return None