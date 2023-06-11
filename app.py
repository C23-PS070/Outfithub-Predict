from flask import Flask, jsonify, request
from utilities import predict_pipeline
from google.cloud import storage
from werkzeug.utils import secure_filename
import json
import uuid

app = Flask(__name__)

storage_client = storage.Client.from_service_account_json('project-capstone.json')
bucket_name = 'upload_outfithub'

@app.route('/', methods=["GET"])
def root():
     if request.method == "POST":
          return jsonify({'message': 'Connection successful', 'status': 'Success'}), 200
     else:
          return jsonify({'error': 'Only GET method is allowed', 'status': 'Failed'}), 405

@app.route("/api/v1/predict", methods=["GET", "POST"])
def predict():
     data = request.get_json()
     prediction = predict_pipeline(data)
     return jsonify(prediction), 200

@app.route("/api/v1/upload", methods=["GET", "POST"])
def upload():
     try:
          storage_client.get_bucket(bucket_name)

          if 'image' not in request.files:
               return jsonify({'error': 'No image file', 'status': 'Failed'}), 400

          image = request.files['image']
          if image.filename == '':
               return jsonify({'error': 'No image selected', 'status': 'Failed'}), 400

          filename = secure_filename(image.filename)
          filename = str(uuid.uuid4()) + '.' + image.filename.rsplit('.', 1)[1]

          blob = storage_client.bucket(bucket_name).blob(filename)
          blob.upload_from_file(image)

          image_url = blob.public_url

          return jsonify({"image_url": image_url}), 200

     except Exception as e:
          return jsonify({'error': 'Connection failed: ' + str(e), 'status': 'Failed'}), 500

if __name__ == "__main__":
     app.run(debug=True)