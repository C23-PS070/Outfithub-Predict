<div align="center">

# OutfitHub Predict

</div>

<br>

## Architecture
<div align="center">
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPc6nTxRF3mr0tb1b_GZJrFNSSn2LG7pY5pV7uvqBVh2lXtcUhV5GNsZsCpaUGIYO2Ww8xOKZhLX4tutI1yKss-eSFjKJqZaGSEVsmfzXlerRMawScuI8UxMcddfkljPARVDAteZ7ri2y0KB1KPtz8sVJV_F4lRDmfLTJKwTLizQNcRbVlfmHxL5u4yg/s320/Untitled-2023-06-16-1707.png"/>
</div>

<br>

## Get Started
### Prerequisites
* Download and install <a href="https://www.python.org/downloads/release/python-395/">Python v3.9.5<a/> <br>
  Make sure your Python and pip are installed:
  ```bash
  python --version
  pip --version
  ```
* Have a Google Cloud Platform account if you want to deploy using GCP.

### Local Installation
* Clone the repository using git:
  ```bash
  git clone https://github.com/C23-PS070/Outfithub-Predict.git
  ```
* Move to project folder:
  ```bash
  cd Outfithub-Predict
  ```
  _Note: You must change the ```PATH_TO_CREDENTIAL``` and ```BUCKET_NAME``` in the app.py file according to what you have created._
  
* Install the packages:
  ```bash
  pip install
  ``` 
* Run the server:
  ```bash
  python app.py
  ``` 

### Dataset
* The dataset we use is the <a href="https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset?datasetId=139630&sortBy=voteCount">Fashion Product Images Dataset<a/> sourced from Kaggle.
* Extract and upload all <a href="https://drive.google.com/drive/folders/1oQb1LImUCdB-wrDUD6KGnBc6f3OntM9s">processing results<a/> to Google Cloud Storage.
  
  _Note: Make sure you have created a Bucket in Google Cloud Storage._
  
### Deployment
* Clone the repository using git:
   ```bash
  git clone https://github.com/C23-PS070/Outfithub-Predict.git
  ```
* Move to project folder:
  ```bash
  cd Outfithub-Predict
  ```
  
  _Note: Make sure you have created a credentials.json from a service account that has permission to access Google Cloud Storage.You must also change the ```PATH_TO_CREDENTIAL``` and ```BUCKET_NAME``` in the app.py file according to what you have created using the Cloud Shell Editor or other text editor._
  
* Build an image:
  ```bash
  gcloud builds submit --tag gcr.io/PROJECT_ID/IMAGE_NAME
  ```
  
   _Note: You must change the ```PROJECT_ID``` and ```IMAGE_NAME``` according to what you want to create._
 
* Make sure the image that has been created is running properly:
  ```bash
   docker run -p 8080:8080 IMAGE_NAME
  ```
  
  _Notes: You must change the ```IMAGE_NAME``` according to the image you have created._
  
* Deploy a Cloud Run service:
  ```bash
  gcloud run deploy SERVICE_NAME \
  --image IMAGE_NAME \
  --platform managed \
  --region REGION \
  --allow-unauthenticated \
  ```
  
   _Notes: You must change the ```SERVICE_NAME```, ```IMAGE_NAME``` and ```REGION``` according to what you want to create._

* Perform the test using the deployed link.

<br>

## Usage
If the server is already running, you can check our <a href="https://documenter.getpostman.com/view/27909743/2s93shz9gL">API Documentation</a> for more details and test it with Postman.

<br>

## Tech Stack
[![Google Cloud Platform](https://img.shields.io/badge/Google%20Cloud%20Platform-%234285F4.svg?style=plastic&logo=google-cloud&logoColor=white)](https://cloud.google.com/) [![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=plastic&logo=kaggle&logoColor=white)](https://www.kaggle.com/) [![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=plastic&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/) [![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=plastic&logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=plastic&logo=docker&logoColor=white)](https://www.docker.com/) [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=plastic&logo=github&logoColor=white)](https://github.com/) [![Postman](https://img.shields.io/badge/Postman-FF6C37?style=plastic&logo=postman&logoColor=white)](https://www.postman.com/) [![Jupyter Notebook](https://img.shields.io/badge/Jupyter-%23FA0F00.svg?style=plastic&logo=jupyter&logoColor=white)](https://jupyter.org/) [![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

<br>

## License
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
