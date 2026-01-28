
#  Django Blog System 

## 🔗 Overview


This project is a Blog System integrated into a Django application where:

Doctors can create and manage blog posts.

Patients can view blog posts, organized by categories.

It is part of the Banao Python Django tasks.




# 🚀 Features

## 🩺 Doctor

* 📝 Can sign up as a doctor.
* 🖊️ Can create blog posts with the following fields:

  * 🏷️ **Title**
  * 🖼️ **Image**
  * 📂 **Category** (e.g., Mental Health, Heart Disease, Covid19, Immunization)
  * 📰 **Summary**
  * ✍️ **Content**
  * 📌 **Status**: Draft or Published
* 👀 Can view posts they have uploaded.
* 🧭 Navigation tailored for doctor users.

## 🧑‍⚕️ Patient

* 📝 Can sign up as a patient.
* 👀 Can view all published posts.
* 📂 Posts are displayed category-wise.
* 📰 Each post preview includes:

  * 🏷️ **Title**
  * 🖼️ **Image**
  * ✂️ **Summary** (truncated to 15 words with `...` if longer)
* 🧭 Navigation tailored for patient users.




## Author

👤 **Author:** Raghu Ram  
🌐 **GitHub:** [raghuram-007](https://github.com/raghuram-007)  



![Author](https://img.shields.io/badge/Author-Raghu%20Ram-blue?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-raghuram--007-black?style=for-the-badge&logo=github&logoColor=white)

# Banao Django Blog System 📝


![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)  
![Django](https://img.shields.io/badge/Django-5.2.8-green?logo=django&logoColor=white)  
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql&logoColor=white)  
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-yellow)  
![Status](https://img.shields.io/badge/Status-Development-orange)


#  🛠️ Technical Details

🐍 Backend: Python 3.x, Django 5.2.8

🗄️ Database: MySQL

🎨 Frontend: Bootstrap 5.3 for styling

📝 Forms: Django forms with widget_tweaks for customization

🔐 Authentication:

👩‍⚕️ Separate signup for Doctor and Patient

🔀 Custom login redirect based on role

🖼️ Media Handling: Upload images using MEDIA_URL and MEDIA_ROOT

👥 User Roles: Managed via UserProfile model (doctor/patient)

## Dependencies

Django >= 5.2

MySQL

widget_tweaks

jazzmin (for admin customization)

Bootstrap 5.3
# Installation

## Clone the repository:

git clone https://github.com/raghuram-007/Banao_python_django_3.git
cd Banao_python_django_3


## Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


## Install dependencies:

pip install -r requirements.txt


## Setup MySQL database:

Create a database named banao_blogdb

Update settings.py with your MySQL credentials

## Run migrations:

python manage.py makemigrations
python manage.py migrate


## Create a superuser (optional):

python manage.py createsuperuser


## Run the development server:

python manage.py runserver


## Access the app:

Doctor login: /login/ → redirected to /my-posts/

Patient login: /login/ → redirected to /posts/
# 🧠 How It Works (URL)


| Path               | Description                       |
| ------------------ | --------------------------------- |
| `/login/`          | Login page                        |
| `/logout/`         | Logout                            |
| `/signup/doctor/`  | Doctor signup                     |
| `/signup/patient/` | Patient signup                    |
| `/create/`         | Doctor: create a blog post        |
| `/my-posts/`       | Doctor: view own posts            |
| `/posts/`          | Patient: view all published posts |

# NOTES


Only doctors can create and manage posts.

Patients can only view published posts.

Post summaries are truncated to 15 words for preview.

Users are redirected automatically based on role after login.
