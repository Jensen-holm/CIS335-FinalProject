# CIS335-FinalProject
Data Mining (CIS-335) final project

### Local Setup
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip3 install -r requirements.txt`

### Run
1. `streamlit run app.py`


### Process
 - Build webcam
 - Set up facial recognition
 - Train ML model to detect Gender


### Training Data

The data itself: `https://www.kaggle.com/datasets/cashutosh/gender-classification-dataset`

The first thing I am planning on doing next is to download these pictures, and then <br>
organize them into their own folders and setup a csv file containing the label (male or female) <br>
and then the image bytes of the photo.

Then hopefully after training a decistion tree I will have a model good enough to tell <br>
wether or not the person using my streamlit app is a male or a female.
