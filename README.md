# Secure-Translator-Platform-Fullstack



________________________________________________________________

## 📑 The Content of the project

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Structure](#structure)
- [Author](#author)

____________________________________________________________

## 📌 Project Overview

Secure fullstack web application with an API backend and an external AI service.

____________________________________________________________

## 🚀 Features

* AI service for translation

+ FastAPI backend

+ Hugging Face Inference API integration

+ JWT Authentication

+ Easy to deploy and extend

____________________________________________________________

## 🏗️ Technologies Used

#### 🎨 Frontend

* React.js

* Vite

* TailwindCSS

* Axios

#### ⚙️ Backend

* FastAPI

* PostgreSQL

* SQLAlchemy

* JWT Authentication

#### 🧠 Machine Learning

* HuggingFace Inference

* Fine-tuning model

####  deployement

* Versel

####  Docker

* Dockerfile

____________________________________________________________

## 🚀 Installation & Lancement

#### 1- Create a virtual environment
```
python3 -m venv myvenv
source myvenv/bin/activate
```
#### 2- install requirements
```
pip install -r requirements.txt
```
#### 3- Create a .env file inside the app folder
```
HF_API_KEY=your_huggingface_api_key
SECRET_KEY=your_jwt_secret_key   
```
#### 4- Run the API

```
uvicorn app.main:app --reload

```
#### 5- Install reactjs

```
Pip install nodejs

```

#### 6- Run the API

```
npm run dev


____________________________________________________________

## 📂 Project Structure

```
```
Application_Analyse-Emotion/
│
├── app/
|   ├── __pycache__.py
│   ├── __init__.py
│   ├── config.py
│   ├── emotion_model.py
│   ├── main.py
│   ├── schemas.py
|   ├── Dockerfile    
│   └── .env
├── react-project 
|   ├── node_module
│   ├── public
|   ├── Dockerfile  
│   └── src
│        ├── assets
│        ├── dash_page
│        ├── login_page     
│        └── main.jsx
├── .gitignore   
├── docker-compose.yml   
├──.env  
├──pytest.ini  
├── requirements.txt
└── README.md

```

____________________________________________________________

## 👩‍💻 Author
<br>

**Mariam BENALI** 

💼  Data Science Student | Machine Learning-Deep Learning Enthusiast

📫 **Contact:**  
- [Email](miriam.bena@gmail.com)  
- [GitHub](https://github.com/mariambenali)

<br>