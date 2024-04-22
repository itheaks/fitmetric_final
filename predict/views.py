from django.shortcuts import render
from django.views import View
import pickle
import os
from django.conf import settings
import pandas as pd
import numpy as np
import joblib
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required()
def Home(request):
    return render(request,"predict/index.html")



class DiseasesPredict(LoginRequiredMixin,View):
    model_path1 = os.path.join(settings.BASE_DIR, "ml_models", "models", "diseases_dt.joblib")
    model_path2 = os.path.join(settings.BASE_DIR, "ml_models", "models", "diseases_rf.joblib")
    model_path3 = os.path.join(settings.BASE_DIR, "ml_models", "models", "diseases_knn.joblib")

    symptoms = [
        "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering",
        "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting",
        "vomiting", "burning_micturition", "spotting_urination", "fatigue", "weight_gain",
        "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy",
        "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes",
        "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish_skin",
        "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain",
        "constipation", "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine",
        "yellowing_of_eyes", "acute_liver_failure", "fluid_overload", "swelling_of_stomach",
        "swelled_lymph_nodes", "malaise", "blurred_and_distorted_vision", "phlegm",
        "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
        "chest_pain", "weakness_in_limbs", "fast_heart_rate", "pain_during_bowel_movements",
        "pain_in_anal_region", "bloody_stool", "irritation_in_anus", "neck_pain", "dizziness",
        "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels",
        "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails", "swollen_extremities",
        "excessive_hunger", "extra_marital_contacts", "drying_and_tingling_lips", "slurred_speech",
        "knee_pain", "hip_joint_pain", "muscle_weakness", "stiff_neck", "swelling_joints",
        "movement_stiffness", "spinning_movements", "loss_of_balance", "unsteadiness",
        "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort", "foul_smell_of_urine",
        "continuous_feel_of_urine", "passage_of_gases", "internal_itching", "toxic_look_(typhos)",
        "depression", "irritability", "muscle_pain", "altered_sensorium", "red_spots_over_body",
        "belly_pain", "abnormal_menstruation", "dischromic_patches", "watering_from_eyes",
        "increased_appetite", "polyuria", "family_history", "mucoid_sputum", "rusty_sputum",
        "lack_of_concentration", "visual_disturbances", "receiving_blood_transfusion",
        "receiving_unsterile_injections", "coma", "stomach_bleeding", "distention_of_abdomen",
        "history_of_alcohol_consumption", "fluid_overload.1", "blood_in_sputum",
        "prominent_veins_on_calf", "palpitations", "painful_walking", "pus_filled_pimples",
        "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
        "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze"
    ]

    disease=['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
        'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
        'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
        'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
        'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
        'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
        'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
        'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
        'Osteoarthristis', 'Arthritis',
        '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
        'Urinary tract infection', 'Psoriasis', 'Impetigo']
    
    def getSymptomsLen(self):
        return len(self.symptoms)
    
    def get(self,request):
        context = {
            'symptoms':self.symptoms
        }
        return render(request,'predict/diseases_l.html',context)
    
    def post(self,request):
        symptoms_list = request.POST.getlist('symptoms[]')
        l2 = [0]*self.getSymptomsLen()
        for k in range(0,self.getSymptomsLen()):
            for z in symptoms_list:
                if(z==self.symptoms[k]):
                    l2[k]=1
        model1 = joblib.load(self.model_path1)
        model2 = joblib.load(self.model_path2)
        model3 = joblib.load(self.model_path3)
        data = pd.DataFrame([l2])
        pred1 = model1.predict(data)[0]
        pred2 = model2.predict(data)[0]
        pred3 = model3.predict(data)[0]
        pred = [self.disease[pred1],self.disease[pred2],self.disease[pred3]]
        guess = f'You have a risk of {max(pred)}'
        context = {
            'result':guess,
        }
        return render(request,'predict/diseases_l.html',context)