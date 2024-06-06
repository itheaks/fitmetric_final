# FitMetric

## Overview

FitMetric is a comprehensive health and fitness application designed to help users manage their health through various features including total daily energy expenditure calculation, food nutrition analysis, disease prediction, prescription scanning, mental health assessment, organ status prediction, doctor appointment booking, health-related blogs, event management, sensor integration, and an AI chatbot.

## Access

- **Webpage**: 
  - http://fitmetric.xyz/
  - https://fitmetric.onrender.com/

- **Android Application**: [Download here](https://drive.google.com/drive/folders/15WLHTPvEbu1Ko2u1QVoh3HvHpdxoCQol?usp=sharing)

- **Source Code**: [GitHub Repository](https://github.com/itheaks/fitmetric_final)

- **Demo Video and Images**: [View here](https://drive.google.com/drive/folders/1ucZiw2I2nZAXxbmX3eK-Djm73JyUvR-7?usp=sharing)

**Note**: If the website does not load immediately, please be patient and wait for about 1 minute, as it may occasionally go to sleep due to inactivity. For login demo, use ID: `aksingh621311@gmail.com` and Password: `12345678`.

## Features

- **Total Daily Energy Expenditure Calculation**: Calculates TDEE and BMI, and provides the required grams of protein, fat, and carbohydrates.
- **Food Nutrition Analysis**: Offers detailed nutritional information for food items.
- **Disease Prediction via Symptoms**: Uses three machine learning models to predict diseases based on symptoms.
- **Prescription Scanning**: Allows users to upload a prescription image to get medicine information.
- **Mental Health Assessment**: Evaluates mental health through situation-based problems for three age categories.
- **Organ Status Prediction**: Predicts health status for heart disease, diabetes, breast cancer, liver disease, and kidney disease.
- **Doctor Connect**: Enables users to book appointments with doctors.
- **Blog**: Provides the latest health-related news.
- **Event Management**: Allows users to create and join events.
- **Sensor Integration**: Monitors data from heart rate monitors, oximeters, and ECG devices.
- **AI Chatbot**: Answers user queries and provides guidance using GPT.

## Installation Guide

To set up the FitMetric project on your local machine, follow the steps below:

### Prerequisites

- Python 3.x
- Django
- Virtualenv

### Steps

1. **Clone the Repository**

    ```
    git clone https://github.com/itheaks/fitmetric_final.git
    cd fitmetric_final
    ```
2. **Create a Virtual Environment**

    ```
    python -m venv venv
    source venv\Scripts\activate
    ```
3. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```
4. **Apply Migrations**

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
5. **Run the Development Server**

    ```
    python manage.py runserver
    Click on 'http://127.0.0.1:8000/'
    ```
## Thank YOU
### For Any query reach to me at aksmlibts@gmail.com
