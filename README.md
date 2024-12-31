# Phisher_Fisher

Phishing is a technique used by hackers to steal valuable information about a user, usually in the form of emails. They appear to the victim as a seemingly real and certified entity and urging them to input important personal information such as their name, credit card number, and social security number on a seemingly official form. However, once the victim submits this form, the information they added to the form is sent directly to the attackers.

Phisher Fisher was created to solve this problem. It's a Google Chrome extension that allows users to quickly validate whether a message they received is suspected of phishing or not from a distil-BERT machine learning model. Upon copy/pasting a message they want to validate, the model will determine the message's status, and return its' classification back to the user.

I was inspired to create Phisher Fisher by taking CS166: Information Security and CS171: Introduction to Machine Learning at San José State University, where I learned about phishing attacks and fundamental machine learning principles respectively.

## How to Run

### Frontend

#### Installing the Vue.js CLI

`npm install -g @vue/cli`

#### Installing Tailwind CSS

`npm install -D tailwindcss@latest postcss@latest autoprefixer@latest`

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

Run the Jupyter Notebook file, which will install a zip folder called "saved_model" containing the model and its' tensors. You don't have to run any of the cells mentioning the base distilBERT model since it is not used, nor any of the cells displaying metrics or graphs.
Make sure the unzipped "saved_model" directory is placed inside the "model" directory, as that is how the MODEL_PATH is set up. 

#### Starting the Service

`python app.py`
