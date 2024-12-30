# Phisher_Fisher

Phishing is a technique used by hackers to steal valuable information about a user, usually in the form of emails. They appear to the victim as a seemingly real and certified entity and urging them to input important personal information such as their name, credit card number, and social security number on a seemingly official form. However, once the victim submits this form, the information they added to the form is sent directly to the attackers.

Phisher Fisher was created to solve this problem. It's a Google  Chrome extension that allows users to quickly validate whether a message they received is suspected of phishing or not from a distil-BERT machine learning model. Upon copy/pasting a message they want to validate, the model will determine the message's status, and return its' classification back to the user.

The creation of Phisher Fisher was primarily inspired by CS 166: Information Security at San José State University, and my previous internship, where I was rountinely sent out phishing training and "test" emails.

## How to Run

### Frontend
#### Installing the Vue.js CLI

`npm install -g @vue/cli`

#### Ensure node_modules is updated

`cd frontend`

`npm install`

#### Building the project

`npm run build`


#### Uploading the project onto Google Chrome
1. Navigate to "chrome://extensions/"
2. Enable "Developer Mode"
3. Select "Load Unpacked", then upload the "dist" directory inside "frontend" (should be created after building the project)


### Backend (Still figuring out :/ )

#### Creating instance of model

Run the Jupyter Notebook file, which will install a zip file containing the model and its' tensors.

#### Starting the Service
`python app.py`

