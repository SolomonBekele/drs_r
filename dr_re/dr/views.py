from django.shortcuts import render
import pandas as pd
import joblib
import os
# from django.conf.settings import PROJECT_ROOT

from django.conf import settings
# Create your views here.
def re_home(request):
     x=[1,2,3,4]
     print("teeeeeeeeel")
     return render(request,'recommendation/re_home.html',{"x":x})


def recommend(request):
     symptom =["high_fever","nausea","skin_rash","yellowish_skin",
                    "itching","mild_fever","vomiting","fatigue",
                    "abnormal_menstruation","muscle_weakness","indigestion",
                    "joint_pain","yellowing_of_eyes","headache","blurred_and_distorted_vision",
                    "continuous_feel_of_urine","prominent_veins_on_calf","sweating", 
                    "altered_sensorium","lack_of_concentration","neck_pain",
                    "irritation_in_anus","abdominal_pain","chills",'shivering','sunken_eyes','breathlessness',
                     'hip_joint_pain','cough','ulcers_on_tongue','dark_urine','loss_of_appetite',
                     'weight_loss','irregular_sugar_level','malaise','rusty_sputum','chest_pain','mucoid_sputum',
                     'diarrhoea','family_history','phlegm','muscle_pain','congestion','patches_in_throat',
                     'unsteadiness','loss_of_balance','stomach_pain','spotting_ urination','dischromic _patches',
                    'dizziness','inflammatory_nails','acidity']
     l=[0]*52
     ll={0: '(vertigo) Paroymsal  Positional Vertigo',1: 'AIDS',2: 'Acne',3: 'Alcoholic hepatitis',
         4: 'Allergy',5: 'Arthritis',6: 'Bronchial Asthma',7: 'Cervical spondylosis',8: 'Chicken pox',
         9: 'Chronic cholestasis',10: 'Common Cold',11: 'Dengue',12: 'Diabetes ',
        13: 'Dimorphic hemmorhoids(piles)',14: 'Drug Reaction',15: 'Fungal infection',16: 'GERD',
        17: 'Gastroenteritis',18: 'Heart attack',19: 'Hepatitis B',20: 'Hepatitis C',
        21: 'Hepatitis D',22: 'Hepatitis E',23: 'Hypertension ',24: 'Hyperthyroidism',25: 'Hypoglycemia',26: 'Hypothyroidism',
        27: 'Impetigo',28: 'Jaundice',29: 'Malaria',30: 'Migraine',31: 'Osteoarthristis',32: 'Paralysis (brain hemorrhage)',
        33: 'Peptic ulcer diseae',34: 'Pneumonia',35: 'Psoriasis',36: 'Tuberculosis',37: 'Typhoid',
        38: 'Urinary tract infection',39: 'Varicose veins',40: 'hepatitis A'}
     if request.method == 'POST':
          # when the form is submitted
          selected_symptom = request.POST.getlist('symptom')
          for i in selected_symptom:
               j=symptom.index(i)
               l[j]=1
          # file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
          ml_model = joblib.load("../dr_re/ml_model/ml_model_new1.joblib")
          # predictions = ml_model.predict(pd.DataFrame(l))
          predictions = ml_model.predict(l)
          # Get the metadata of the model
          # num_cols = ml_model.get_feature_importance().shape[0]
          # num_rows = ml_model.tree_count_

          # print(f"Number of columns in the model: {num_cols}")
          # print(f"Number of rows in the model: {num_rows}")
          disease = ll[predictions.tolist()[0]]
          print (predictions)

          return render(request, 'recommendation/recommend.html', {'symptom': symptom, 'disease': disease})
     return render(request, "recommendation/recommend.html",{'symptom': symptom})
